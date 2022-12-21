import django_filters
from leave.models import AvailableLeaves


class lopFilter(django_filters.FilterSet):
    month = django_filters.DateFilter(field_name="dateTime" ,lookup_expr='date__gte')

    class Meta:
        model = AvailableLeaves
        fields = ['employee__dept']

    
