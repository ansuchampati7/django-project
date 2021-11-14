from django.contrib.admin.decorators import register
from django.contrib.admin.sites import AlreadyRegistered
from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from .models import addusers
from authentication.models import addblog


def homei(request):
    if request.session.get('islogin'):
        return render(request,"afterlogin.html")
    return render(request,"home.html")

    

def logini(request):
    return render(request,"login.html")

def signin(request):
    return render(request,"signin.html")

def aftersignin(request):
    if request.method == "GET" :
        return redirect("signin/")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = request.POST.get('username')
        try:
            addusers.objects.get(email=email)
        except:
            addusers.objects.create(username=username, password=password, email=email )
            msg = "Registered successfully..."
            return render(request,"signin.html", {'msg':msg})
        else:
            msg =" Already registered  successfully..."
            return render(request,"signin.html", {'msg':msg})
    

def afterlogin(request):
    if request.method == "GET" :
        if request.session.get('email'):
            all = addblog.objects.all()
            return render(request,"afterlogin.html", {'all':all})
        else:
            return redirect("logini/")
    else:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            addusers.objects.get(email=email)
        except:
            msg="You are not registered...Plz signin"
            return render(request,"login.html", {'msg':msg})
        else:
            all = addblog.objects.all()
            x= addusers.objects.get(email=email)
            if x.email==email and x.password==password and all :
                request.session['islogin']= "True"
                request.session['email']=email
                
                return render(request,"afterlogin.html", {'all':all})
            
      
def logout(request):
    del request.session['islogin']
    del request.session['email']
    return render(request,"home.html")