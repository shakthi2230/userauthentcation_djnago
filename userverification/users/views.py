from django.shortcuts import render  ,redirect, reverse
from django.http import HttpResponse
from pathlib import Path
import os
from.models import UserProfile
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def home(request):
    
    return  render(request,'landingpage.html')

def createaccount(request):
    if request.method == 'POST':
        name = request.POST["name"]
        email = request.POST["email"]
        address = request.POST["address"]
        contact = request.POST["phonenumber"]
        password = request.POST["password"]

        
        existing_user = UserProfile.objects.filter(email=email).exists()

        if existing_user:
            messages.error(request, f' {email} This Email Id already exists. Please use a different email.')
            return redirect('createaccount')
        else:
            
            obj = UserProfile(
                name=name,
                address=address,
                mobile_number=contact,
                email=email,
                password=password
            )
            obj.save()

            messages.success(request, f'Hello {name}, your account was created successfully. You can now log in.')
            return redirect('login')

    return render(request, 'signup.html')

#login function
    
def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = UserProfile.objects.get(email=email, password=password)
            if user:
                messages.warning(request, f"Welcome, {user.name}!")
                return render(request, 'login.html',{'name':user.name}) 
            else:
                
                return render(request, 'wronguser.html') 
            
           
        except UserProfile.DoesNotExist:
            messages.success(request, "Invalid email or password. Please try again")
            
            return  render(request,'signin.html')
    return  render(request,'signin.html')

def records(request):
    mydata=UserProfile.objects.all()
    return render(request,'records.html', {"mydata":mydata})

def deletedata(request,id):
     deletedatas=UserProfile.objects.get(id=id)
     deletedatas.delete()
     return redirect('records') 

def forgotpassword(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("phonenumber")
        
        try:
           
            user = UserProfile.objects.get(email=email, name=name, mobile_number=contact)

            if user:
                return render(request, 'update.html', {'getdata': user})
            else:
                messages.error(request, "Invalid email, name, or contact. Please try again.")
                return redirect('forgotpassword') 
            
        except UserProfile.DoesNotExist:
            messages.error(request, "Invalid email, name, or contact. Please try again.")
            return redirect('forgotpassword')

    return render(request, 'forgotpassword.html')

def updatepassword(request,id):
    getdata=UserProfile.objects.get(id=id)
    if request.method=='POST':
        # name = request.POST["name"]
        # email = request.POST["email"]
        # address = request.POST["address"]
        # contact = request.POST["phonenumber"]
        password=request.POST["password"]

        # getdata.name=name
        # getdata.address=address
        # getdata.mobile_number=contact
        # getdata.email=email
        getdata.password=password
        getdata.save()
        messages.success(request, 'Password reset successful. You can now log in with your new password.')
        return redirect('home')

