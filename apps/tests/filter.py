from rest_framework_filters import FilterSet, NumberFilter

from .models import Answer


class ActorFilter(FilterSet):
    test = NumberFilter(field_name='question__test__id')

    class Meta:
        model = Answer
        fields = {
            'test': ['icontains', ],
        }