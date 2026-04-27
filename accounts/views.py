from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        password = request.POST.get('pass1')

        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home')
        
        messages.error(request,'username or password incorrect...')

    return render(request,'login.html')


def logout_user(request):
    if request.user:
        logout(request)
        return redirect('login')


def register_view(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        uname = request.POST.get('uname')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        if pass1 != pass2:
            messages.error(request,'Password not match')
            return redirect('register')
        
        if User.objects.filter(username=uname).exists():
            messages.error(request,'username already exists')
            return redirect('register')
        
        user = User.objects.create_user(
            first_name = fname,
            last_name = lname,
            username = uname,
            password = pass1,
        )
        user.save()
        messages.success(request,'user registered successfully...')
        return redirect('login')

    return render(request,'register.html')


