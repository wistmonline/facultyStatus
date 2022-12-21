from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from  .models import AvailableLeaves, Leave
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import datetime



# Create your views here.
@login_required(login_url="loginUser")
def applyLeave(request):
   
    if request.method == 'POST':
        # formatNumber = lambda n: n if n%1 else int(n)
        employee = request.user
        no_of_days = request.POST.get('halfday')
        emergency = request.POST.get('emergency-leave')
        fromdate = request.POST.get('fromdate')
        todate = request.POST.get('todate')
        reason = request.POST.get('reason')
        category = request.POST.get('category')

        if not no_of_days:
            if emergency:
                no_of_days = 1.5
                print("Entered.... emergency.")
                leave = Leave.objects.create(
                employee = employee,
                no_of_days = no_of_days,
                from_date = datetime.date.today(),
                reason = reason,
                category = category,
                emergency = True,
            )
            else :
                no_of_days = request.POST.get('no-of-days') 

                leave = Leave.objects.create(
                    employee = employee,
                    no_of_days = no_of_days,
                    from_date = fromdate,
                    to_date = todate,
                    reason = reason,
                    category = category,
                )
        else:
            leave = Leave.objects.create(
            employee = employee,
            no_of_days = no_of_days,
            from_date = fromdate,
            reason = reason,
            category = category,
            )
        leave.save()
        return redirect('leaveStatus')

    try:
        availableLeaves = AvailableLeaves.objects.get(employee = request.user)
    except:
        return HttpResponse("Someting went wrong...")

    context = {
        'al': availableLeaves,
    }
    return render(request, 'leave/apply_leave.html', context)


@login_required(login_url="loginUser")
def leaveStatus(request):

    leaves = Leave.objects.filter(employee=request.user).order_by("-applied_time")
    try:
        availableLeaves = AvailableLeaves.objects.get(employee = request.user)
    except:
        return HttpResponse("Someting went wrong, contact Gowtham Tirri WISTM CSE")

    context = {
        'al': availableLeaves,
        'leaves':leaves
    }
    return render(request, 'leave/leave_status.html', context)


def leaveRejectHod(request, pk):
    try:
        leave = Leave.objects.get(id=pk)
        leave.hod_approved = False
        leave.principal_approved = False
        leave.save()
    except:
        return HttpResponse("Something went wrong.. Try again")
    messages.warning(request, "Leave Rejected")
    return redirect('leaveRequestsForHod')    


def leaveApproveHod(request, pk):
    try:
        leave = Leave.objects.get(id=pk)
        leave.hod_approved = True
        leave.save()
    except:
        return HttpResponse("Something went wrong.. Try again")
    messages.success(request, "Leave Approved, Request has been sent to Principal Sir")
    return redirect('leaveRequestsForHod')    


def leaveApprovePrincipal(request, pk):
    try:
        leave = Leave.objects.get(id=pk)
        leave.principal_approved = True
        ndays = leave.no_of_days 
        al = AvailableLeaves.objects.get(employee=leave.employee)

# ===== Leave Category Alogrithm ======= Auto Decrease Available  leaves hierarichally
        # If casuall leves are ZERO avialabel do this
        if al.casual_leaves <= 0:
            # if copenstation leaves are ZERO do this
            if al.compensation_leaves <=0:
                # if earn leaves are ZERO do this
                if al.earn_leaves <=0:
                    al.loss_of_pay += ndays
                else:
                    # if earn leaves less than no of day required do this
                    if al.earn_leaves <= ndays:
                        ndays = ndays - al.earn_leaves                    
                        al.earn_leaves -= al.earn_leaves
                        al.loss_of_pay += ndays 
                    # if earn leaves available
                    else:
                        al.earn_leaves -= ndays 
            # casula leaves are ZERO and compensation leaves available
            else:
                if al.compensation_leaves <= ndays:
                    ndays = ndays - al.compensation_leaves
                    al.compensation_leaves -= al.compensation_leaves
                    if al.earn_leaves <= ndays:
                        ndays = ndays - al.earn_leaves                    
                        al.earn_leaves -= al.earn_leaves
                        al.loss_of_pay += ndays 
                    else:
                        al.earn_leaves -= ndays 
                else:
                    al.compensation_leaves -= ndays 
        # casulal leaves are available                   
        else:
            # casual leaves are less than no of days required
            if al.casual_leaves <= ndays:
                ndays = ndays - al.casual_leaves
                al.casual_leaves -= al.casual_leaves
                if al.compensation_leaves <= ndays:
                    ndays = ndays - al.compensation_leaves
                    al.compensation_leaves -= al.compensation_leaves
                    if al.earn_leaves <= ndays:
                        ndays = ndays - al.earn_leaves                    
                        al.earn_leaves -= al.earn_leaves
                        al.loss_of_pay += ndays 
                    else:
                        al.earn_leaves -= ndays 
                else:
                    al.compensation_leaves -= ndays              
            # casual leaves available as no of days
            else:
                al.casual_leaves -= ndays

        al.save()
        leave.save()
    except:
        return HttpResponse("Something went wrong.. Try again")
    messages.success(request, "Leave Approved")
    return redirect('leaveRequestsForPrincipal')    


def leaveRejectPrincipal(request, pk):
    try:
        leave = Leave.objects.get(id=pk)
        leave.principal_approved = False
        leave.save()
    except:
        return HttpResponse("Something went wrong.. Try again")
    messages.warning(request, "Leave Rejected")
    return redirect('leaveRequestsForPrincipal')    


def assignLeaves(request):

    faculty_list = AvailableLeaves.objects.filter(employee__dept=request.user.dept)

    for faculty in faculty_list:
        faculty.casual_leaves = 8

    context = {}
    return render(request, 'dashboards/assignLeaves.html', context)