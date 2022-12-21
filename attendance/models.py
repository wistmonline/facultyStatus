from datetime import time
from django.db import models
from accounts.models import Account
from django.utils import timezone

# Create your models here.


LOCATIONS = (
    ("College Campus","College Campus"),
    ("AU","AU"),
    ("Counselling Duty","Counselling Duty"),
    ("Admission work","Admission work"),
    ("On Duty","On Duty"),
    ("Permission","Permission"),
    ("Leave","Leave"),
    ("other","other"),
)

class Attendance(models.Model):
    employee = models.ForeignKey(Account, on_delete=models.CASCADE, null=True)
    location = models.CharField(choices=LOCATIONS, max_length=100)
    other = models.CharField(max_length=300, blank=True, null=True)
    latitude = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    dateTime = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.employee)


    @property
    def maplink(self):
        return f"https://maps.google.com/?q={self.latitude},{self.longitude}"    