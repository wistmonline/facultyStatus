from .models import Leave

def leaveRequestCount(request):
    count = ""
    if request.user.is_authenticated:
        if request.user.is_admin:
            count = Leave.objects.filter(principal_approved=None, hod_approved=True).count()
        elif request.user.is_staff:    
            count = Leave.objects.filter(hod_approved=None).count()

    return {'leaveRequestCount' : count} 