from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def new(request):
    if request.method=='POST':
        username=request.POST['username']
        password =request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user  is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
            return redirect('new')
    return render(request,'new.html')

def register(request):
    if request.method=='POST':
        username =request.POST["username"]
        first_name =request.POST["first_name"]
        last_name= request.POST["last_name"]
        email=request.POST["email"]
        password=request.POST["password"]
        c_password=request.POST["c_password"]
        if password==c_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username  already taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already taken')
            else:
                user=User.objects.create_user(
                username=username,
                first_name=first_name,
                last_name=last_name,
                email=email,
                password=password,)
                user.save();
                return redirect('new')

        else:
            messages.info(request, 'password missmatching')
            return redirect('/')
    return render(request,'register.html')

# Create your views here.
def logout(request):
    auth.logout(request)
    return redirect('/')