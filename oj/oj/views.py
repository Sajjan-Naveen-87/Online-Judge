from django.urls import path
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse,redirect
from django.http import HttpResponse

def indexPage(request):
    return render(request,'home/index.html') 

def handleSignup(request):
    if request.method == 'POST':
        
        # try block
        username=request.POST['signupUsername']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        gender=request.POST['gender']
        #is pass1 alplhanumeric?
        if not username.isalnum(): #str.alnum() returns True if all characters in the string are alphanumeric (letters A-Z, a-z, and numbers 0-9) else return false
            return messages.error(request,'Username must be Alphanumeric !!!')
            return redirect('signup')

        if not fname.isalnum() or not lname.isalnum():
            messages.error(request ,'First Name and Last Name must be Alphanumeric !!!')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists. please choose another ")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')
        #email verifying part to be added

        #appending data to db

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        # myuser.gender=gender # not storing for now
        myuser.save() # saving data
        messages.success(request,'Account created Successfully !!')
        login(request,myuser) #admin login
        return render(request,'home/home.html')
            
    else :
        return HttpResponse(f'<h1>404 not found or username Exist Already</h1>')

def handleLogin(request):
    if request.method == 'POST':
        loginusername=request.POST['loginUsername']
        loginpassword=request.POST['password']
        #checks for username and password
        user=authenticate(username=loginusername,password=loginpassword)
        if not user is None:
            login(request,user) #admin login
            return render(request,'home/home.html')
        # checks for username and password validation
    else:
        return HttpResponse('<h1>404 not found </h1>')
    
def logout(request):
    logout(request) # admin logout
    messages.success(request,'Successfully Logged Out')
    return redirect(request,'')