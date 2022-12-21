import django_filters
from .models import AvailableLeaves


class AvailableLeavesFilter(django_filters.FilterSet):
   
    class Meta:
        model = AvailableLeaves
        fields = ['employee']

    
