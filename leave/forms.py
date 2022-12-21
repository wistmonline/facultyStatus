from django import  forms
from django.db import models
from django.db.models import fields
from .models import Leave

class LeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = "__all__"
