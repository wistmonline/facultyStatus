from django.urls import path
from . import views

urlpatterns = [
    path('facutly', views.facutlyDashboard, name='facultyDashboard' ),
    path('faculty', views.facutlyDashboard, name='facultyDashboard' ), 
    path('principal', views.principalDashboard, name='principalDashboard' ), 
    path('hod', views.hodDashboard, name='hodDashboard' ), 
    path('facultyStatus', views.facultyStatus, name='facultyStatus' ), 
    path('hod/leave/requests', views.leaveRequestsForHod, name='leaveRequestsForHod' ), 
    path('principal/leave/requests', views.leaveRequestsForPrincipal, name='leaveRequestsForPrincipal' ), 
]
