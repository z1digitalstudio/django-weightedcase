# django-weightedcase

django-weightedcase extends django Case and When to be able to obtain a weighted queryset.

# Dependencies
It requires Django >= 1.7.

# Installation
$ pip install git+https://github.com/commite/django-weightedcase.git#egg=django-weightedcase-1.0

# Usage
There are two basic classes: WeightedCase and WeigthedWhen. The usage is very similar to django's Case and When. 
The main difference is that weight should be added to each When. It's possible to define a var_name to save the weight.

In utils there is a method to ponderate a queryset with WeightedCases.

# Example

Let's suposse a model called House, whose fields are rent(Decimal), rooms(Integer), and baths(Decimal).

Now, let's supposse this use case:

"We want to find houses with 3 or more rooms, rent lower or equal than 600, and more than 1 bath. We would be also
interested in houses with 2 rooms, but we preffer 3 or more."

Our queryset will be queryset=House.objects.all()

We will ponderate the queryset like this:
```
  from weightedcase.models import WeightedCase, WeightedWhen
  from weightedcase.utils import ponderate_queryset

  qs = ponderate_queryset(
    queryset,
    WeightedCase(
        WeightedWhen(
            'rent__lte',
            600
        )
    ),
    WeightedCase(
        WeightedWhen(
            'rooms__gte',
            3
        ),
         WeightedWhen(
            'rooms',
            2,
            weight=0.5
        )
    ),
    WeightedCase(
        WeightedWhen(
            'baths__gt',
            1.0
        )
    )
  )
```
After this, every house in our queryset will have annotated the property weight. By default, every weight when add 1 if it's true,
but we can change it as we see when we're looking rooms with 2 rooms. In this case, it will be added 0.5 instead of 1.

We will have 7 possibilities:
  - Weight 0: No conditions are true.
  - Weight 0.5: House has two rooms.
  - Weight 1: Only one of the conditions is true
  - Weight 1.5: House has two rooms and house has more than one bath or rent is lower or eq than 600.
  - Weight 2: Two of the conditions are true.
  - Weight 2.5: House has two rooms, more than one bath and rent is lower or eq than 600.
  - Weight 3: House matches three conditions. House has 3 or more rooms, rent is lower or eq than 600 and house has more than 1 bath.
  
 It's also possible to define another var name, to store a different weight in the same call. We will use the same example as before,
 but we will store the room's weight in a different variable. We would do it like this:
 
 ```
 from weightedcase.models import WeightedCase, WeightedWhen
 from weightedcase.utils import ponderate_queryset
 
 qs = ponderate_queryset(
    queryset,
    WeightedCase(
        WeightedWhen(
            'rent__lte',
            600
        )
    ),
    WeightedCase(
        WeightedWhen(
            'rooms__gte',
            3
        ),
         WeightedWhen(
            'rooms',
            2,
            weight=0.5
        ),
        var_name="roomweight"
    ),
    WeightedCase(
        WeightedWhen(
            'baths__gt',
            1.0
        )
    )
  )
 ```
 In this case, every house will have a 'weight' with a value of 0, 1 or 2, and 'roomweight' 
 with value of 0, 0.5 or 1. 
