from django.db.models import FloatField, Value


def ponderate_queryset(queryset, *cases):
    if not cases:
        raise ValueError("At least one case is required")
    var_names = set([case.var_name for case in cases])
    d_dict = {}
    for var_name in var_names:
        d_dict.update({
            var_name: Value(
                0.0,
                output_field=FloatField())
        })
    queryset = queryset.annotate(**d_dict)
    for case in cases:
        queryset = queryset.annotate(
            **{
                case.var_name: case.to_case()
            }
        )
    return queryset
