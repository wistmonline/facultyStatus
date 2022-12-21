from django.contrib import admin
from .models import Leave, AvailableLeaves

# Register your models here.
class AvailableLeavesAdmin(admin.ModelAdmin):
    list_display = ["employee","casual_leaves","earn_leaves","compensation_leaves", "loss_of_pay"]

class LeavesAdmin(admin.ModelAdmin):
    list_display = ["employee","no_of_days","from_date","to_date","category","hod_approved", "principal_approved"]

admin.site.register(AvailableLeaves, AvailableLeavesAdmin)
admin.site.register(Leave, LeavesAdmin)