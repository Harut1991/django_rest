from rest_framework_filters import FilterSet, NumberFilter

from .models import Answer

class BaseFilter(object):
    def filter_test(self, queryset, name, value):
        return queryset.filter(question__test__id=value)

class TestFilter(FilterSet, BaseFilter):
    test = NumberFilter(field_name='id', method='filter_test')

    class Meta:
        model = Answer
        fields = {
            'test': ['icontains', ],
        }