from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from attendance.filter import AttendanceFilter
from leave.filter import AvailableLeavesFilter
from attendance.models import Attendance
import datetime 
from leave.models import AvailableLeaves, Leave
# Create your views here.

    
@login_required(login_url='loginUser')
def facutlyDashboard(request):
    attendances = Attendance.objects.filter(employee =  request.user).order_by('-dateTime')
     
    context = {"attendances":attendances}
    return render(request, 'dashboards/faculty_dashboard.html', context)    

    
@login_required(login_url='loginUser')
def hodDashboard(request):
    if not request.user.is_staff:
        return HttpResponse("you was not authorised to access this page")

    dt = datetime.datetime.today()
    today = datetime.datetime.today()
    start = dt.replace(hour=0, minute=0, second=0, microsecond=0)


    in_college_campus = Attendance.objects.filter(dateTime__gte=start,  location='College Campus', employee__dept=request.user.dept).count()
    in_au = Attendance.objects.filter(dateTime__gte=start,  location='AU', employee__dept=request.user.dept).count()
    in_counselling = Attendance.objects.filter(dateTime__gte=start,  location='Counselling Duty', employee__dept=request.user.dept).count()
    in_admission_work = Attendance.objects.filter(dateTime__gte=start,  location='Admission work', employee__dept=request.user.dept).count()
    in_duty = Attendance.objects.filter(dateTime__gte=start,  location='On Duty', employee__dept=request.user.dept).count()
    in_permission = Attendance.objects.filter(dateTime__gte=start,  location='Permission', employee__dept=request.user.dept).count()
    in_leave = Attendance.objects.filter(dateTime__gte=start,  location='Leave', employee__dept=request.user.dept).count()
    In_other = Attendance.objects.filter(dateTime__gte=start,  location='other', employee__dept=request.user.dept).count()

    attendances = Attendance.objects.filter(dateTime__year=today.year, dateTime__month = today.month, employee__dept=request.user.dept).order_by("-dateTime")    

    if 'location' in request.GET:
        attendances = Attendance.objects.all().order_by('-dateTime')
        attendanceFilter = AttendanceFilter(request.GET, queryset=attendances)
        attendances = attendanceFilter.qs

    filterForm = AttendanceFilter()

    context = {
        "college_campus":in_college_campus,
        "au":  in_au,
        "counselling": in_counselling,
        "admission_work":  in_admission_work,
        "duty": in_duty,
        "permission":in_permission,
        "leave": in_leave,
        "other":  In_other,
        "attendances":attendances,
        "filterForm":filterForm.form,
    }

    return render(request, 'dashboards/hod_dashboard.html', context)    


@login_required(login_url='loginUser')
def leaveRequestsForHod(request):
    requests = Leave.objects.filter(hod_approved="",employee__dept=request.user.dept).order_by('-applied_time')

    context = {
        'requests':requests
        }
    return render(request, 'dashboards/leave_requests.html', context)    


@login_required(login_url='loginUser')
def leaveRequestsForPrincipal(request):
    requests = Leave.objects.filter(hod_approved=True, principal_approved="").order_by('-applied_time')

    context = {
        'requests':requests
        }
    return render(request, 'dashboards/leave_requests.html', context)    


@login_required(login_url='loginUser')
def facultyStatus(request):
    filterForm = AvailableLeavesFilter()
    if request.user.is_admin:
        faculty_list = AvailableLeaves.objects.all()
        male_faculty = AvailableLeaves.objects.filter(employee__gender='MALE').count()
        female_faculty = AvailableLeaves.objects.filter(employee__gender='FEMALE').count()

        context = {
            'male_faculty':male_faculty,
            'female_faculty':female_faculty,
            'faculty_list':faculty_list,
        }
    elif request.user.is_staff:
        faculty_list = AvailableLeaves.objects.filter(employee__dept=request.user.dept)

        context = {
            'faculty_list':faculty_list,
            }
    return render(request, 'dashboards/faculty_status.html', context)


@login_required(login_url='loginUser')
def principalDashboard(request):
    if not request.user.is_admin:
        return HttpResponse("you was not authorised to access this page")

    today = datetime.datetime.today()
    dt = datetime.datetime.today()
    start = dt.replace(hour=0, minute=0, second=0, microsecond=0)

    in_college_campus = Attendance.objects.filter(dateTime__gte=start, location='College Campus').count()
    in_au = Attendance.objects.filter(dateTime__gte=start,  location='AU').count()
    in_counselling = Attendance.objects.filter(dateTime__gte=start,  location='Counselling Duty').count()
    in_admission_work = Attendance.objects.filter(dateTime__gte=start,  location='Admission work').count()
    in_duty = Attendance.objects.filter(dateTime__gte=start,  location='On Duty').count()
    in_permission = Attendance.objects.filter(dateTime__gte=start,  location='Permission').count()
    in_leave = Attendance.objects.filter(dateTime__gte=start,  location='Leave').count()
    In_other = Attendance.objects.filter(dateTime__gte=start,  location='other').count()

    attendances = Attendance.objects.filter(dateTime__year=today.year, dateTime__month = today.month).order_by("-dateTime")    

    if 'location' in request.GET:
        attendances = Attendance.objects.all().order_by('-dateTime')
        attendanceFilter = AttendanceFilter(request.GET, queryset=attendances)
        attendances = attendanceFilter.qs

    filterForm = AttendanceFilter()

    context = {
        "college_campus":in_college_campus,
        "au":  in_au,
        "counselling": in_counselling,
        "admission_work":  in_admission_work,
        "duty": in_duty,
        "permission":in_permission,
        "leave": in_leave,
        "other":  In_other,
        "attendances":attendances,
        "filterForm":filterForm.form,
    }

    return render(request, 'dashboards/principal_dashboard.html', context)    


def hodFacultyReport(request):

    leaves = Leave.objects.filter(employee=request.user.dept)

    context = {'leaves':leaves}
    return render(request, 'facultyReport.html', context)