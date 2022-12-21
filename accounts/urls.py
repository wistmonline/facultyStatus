from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup, name='signup' ),
    path('loginUser', views.loginUser, name='loginUser' ),
    path('logoutUser', views.logoutUser, name='logoutUser' ),
]
