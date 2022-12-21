from django.shortcuts import redirect
from django.http import HttpResponse


def allowed_users(allowed_users):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            authorised = False
            for group in request.user.groups.all():
                if group.name in allowed_users:
                    authorised =True
            if authorised:
                return view_func(request, *args, **kwargs)                    
            if request.user.is_admin:
                return redirect('principalDashboard')
            if request.user.is_staff:
                return redirect('hodDashboard')
              
            return HttpResponse(' You was not authorised to view  this pages')

        return wrapper_func
    return decorator
