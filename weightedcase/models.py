from django.db.models import When, Case, F, FloatField


########################
# Weighted queryset
########################
class WeightedWhen(object):
    query = ''
    value = None
    weight = 1

    def __init__(self, query, value, weight=1):
        self.query = query
        self.value = value
        self.weight = weight

    def to_when(self, var_name='weight'):
        return When(
            **{
                self.query: self.value,
                'then': F(var_name) + self.weight
            }
        )


class WeightedCase(object):
    conditions = []
    var_name = ''

    def __init__(self, *args, **extra):
        conds = []
        var_name = extra.pop('var_name', 'weight')
        for cond in args:
            if not isinstance(cond, WeightedWhen):
                raise ValueError("Arguments must be of type WeightedWhen")
            conds.append(cond)
        self.conditions = conds
        self.var_name = var_name

    def to_case(self):
        return Case(
            *[cond.to_when(self.var_name) for cond in self.conditions],
            default=F(self.var_name),
            output_field=FloatField(),
            disctint=True
        )
