from django_filters import CharFilter, filters
from rest_framework_filters import FilterSet

from .models import Test, Answer


class ActorFilter(FilterSet):

    class Meta:
        model = Answer
        fields = {
            'question__test__id': ['icontains', ],
        }