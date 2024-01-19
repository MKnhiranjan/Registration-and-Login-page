from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
def loginpage(request):
    page='login'
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username)
        try:
            user=User.objects.get(username=username)
        except:
            messages.error(request,"user doesnot exist")
        user=authenticate(request,username=username,password=password)
        if user!=None:
            login(request,user)
            return render(request,'home.html',{'user':user})
        else:

            return redirect("login")
    else:
        return render(request,'index.html',{'page':page})
    
def logoutPage(request):
    logout(request)
    return redirect('index.html')

def registrationpage(request):
    page='register'
    form=UserCreationForm()
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        # print(user)
        if form.is_valid():
            user=form.save()
            user.save()
            login(request,user)
            return render(request,'home.html',{'user':user})
        else:
            messages.error(request,"Enter a valid username and password")
            return redirect('registration')
    return render(request,'index.html',{'form':form,'page':page})