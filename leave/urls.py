from django.urls import path
from . import views

urlpatterns = [
    path('apply', views.applyLeave, name="applyleave"),
    path('status', views.leaveStatus, name="leaveStatus"),
    path('hod/reject/<str:pk>', views.leaveRejectHod, name="leaveRejectHod"),
    path('hod/approved/<str:pk>', views.leaveApproveHod, name="leaveApproveHod"),
    path('principal/reject/<str:pk>', views.leaveRejectPrincipal, name="leaveRejectPrincipal"),
    path('principal/approved/<str:pk>', views.leaveApprovePrincipal, name="leaveApprovePrincipal"),
    # path('hod/assignLeaves', views.assignLeaves, name="assignLeaves"),
    # Assign Casual leaves to all (=== OR ===) Assign leaves!!
]
 