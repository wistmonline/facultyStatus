from django.contrib import admin
from .models import Attendance

# Register your models here.
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ["name","location", "dateTime", "maplink"]
    list_filter = ("dateTime",   "location")
    search_fields = ['name',  "location"]

    def name(self, obj):
        return obj.employee.name

admin.site.register(Attendance,AttendanceAdmin)