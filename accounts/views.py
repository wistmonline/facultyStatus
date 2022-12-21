from django.shortcuts import render, redirect
from .forms import  RegistrationForm
from .models import Account
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from attendance.models import Attendance
from leave.models import AvailableLeaves

# Create your views here.
@unauthenticated_user
def signup(request):
    signupForm = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            dept = form.cleaned_data['dept']
            gender = form.cleaned_data['gender']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            if password == confirm_password:
                user = Account.objects.create_user(email=email, name=name, dept=dept,gender=gender,phone=phone, password=password)

                user.save()
                availableLeaves = AvailableLeaves.objects.create(employee = user, casual_leaves=8, earn_leaves=0, compensation_leaves=0,loss_of_pay=0)
                availableLeaves.save()
                login(request, user)

                attendances = Attendance.objects.filter(employee =  request.user).order_by('-dateTime')

                context = {"attendances":attendances}
                return redirect("home")
        else:
            return render(request, 'signup.html', context={"message":"Account Already Exist","signupForm":signupForm})

    context = {
        "signupForm":signupForm
    }
    return render(request, 'signup.html', context) 


@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)
            if request.user.is_admin:
                return redirect('principalDashboard')
            if request.user.is_staff:
                return redirect('hodDashboard')
            return redirect('home')
        else:
            context = {"message" :'User name or Password was incorrect'}
            return render(request, 'login.html', context)

    return render(request, 'login.html')


@login_required(login_url="loginUser")
def logoutUser(request):
    logout(request)
    return redirect('loginUser')

