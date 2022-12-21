import django_filters
from .models import Attendance


class AttendanceFilter(django_filters.FilterSet):
    startDate = django_filters.DateFilter(field_name="dateTime" ,lookup_expr='date__gte')
    endDate = django_filters.DateFilter(field_name="dateTime", lookup_expr='date__lte')

    class Meta:
        model = Attendance
        fields = ['employee__dept', 'location']

    
