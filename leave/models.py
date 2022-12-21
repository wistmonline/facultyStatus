from pyexpat import model
from re import T
from django.db import models
from accounts.models import Account

# Create your models here.
class AvailableLeaves(models.Model):
    employee = models.OneToOneField(Account, on_delete=models.CASCADE)
    casual_leaves = models.FloatField(null=True)
    earn_leaves = models.FloatField(null=True)
    compensation_leaves = models.FloatField(null=True)
    loss_of_pay = models.FloatField(null=True)

    def _str__(self):
        return self.teacher


class Leave(models.Model): 
    employee = models.ForeignKey(Account, on_delete=models.CASCADE)
    no_of_days = models.FloatField(null=True, blank=True)
    hod_approved = models.BooleanField(null=True)
    principal_approved = models.BooleanField(null=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    category = models.CharField(blank=True, null=True, max_length=100)
    reason = models.CharField(max_length=500, blank=True)
    applied_time = models.DateTimeField(auto_now_add=True)
    emergency = models.BooleanField(default=False, null=True, blank=True)  

    def formatNumber(self):
        if self.no_of_days % 1 == 0:
            return self.no_of_days
        else: 
            return int(self.no_of_days)    
    
 