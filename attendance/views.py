from re import I
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .forms import AttendanceForm
from .models import Attendance
import datetime 
from .decorators import allowed_users

 

# Create your views here.
@login_required(login_url='loginUser')
def home(request):
    if request.user.is_admin:
        return redirect('principalDashboard')
    if request.user.is_staff:
        return redirect('hodDashboard') 
           
    form = AttendanceForm()
    if request.method == "POST":
        # Get all inputs from form
        location = request.POST['location']
        other = request.POST.get('other')
        latitude = request.POST['latitude']
        longitude = request.POST['longitude']

        # to avoid multiple submissions within 30minutes
        time_threshold = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(minutes=30)
        results = Attendance.objects.filter(dateTime__gt=time_threshold, employee=request.user)
        
        if not results:
            new_attendance = Attendance.objects.create(
                employee  = request.user,
                location = location,
                other = other,
                latitude = latitude,
                longitude = longitude,
            )
            new_attendance.save()
            return redirect('facultyDashboard')
        else:
            context = {"form":form, "message": "You already submitted the attendance in last 30 minutes"}
            return render(request, 'home.html', context)

    context = {"form":form}
    return render(request, 'home.html', context)
    
