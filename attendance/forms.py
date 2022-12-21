from django.forms import ModelForm
from .models import Attendance

# Create the form class.
class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = [ 'location', 'latitude', 'longitude',]
