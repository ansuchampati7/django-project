from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from django.views import View
from .models import addblog
from interface.models import addusers



def myblogs(request):
    my = addblog.objects.filter(author= addusers.objects.get(email=request.session.get('email')))
    return render(request,"afterlogin.html", {'all': my})

def addblogs(request):
    return render(request,"addblogs.html")

class submit(View):
    def get(self, request):
        return redirect("/user/addblogs/")

    def post(self, request):
        tittle = request.POST.get('tittle')
        post = request.POST.get('post')
        author = addusers.objects.get(email=request.session.get('email'))
        if tittle and post :
            addblog.objects.create(tittle=tittle, post=post,author=author)
            msg="Ok boss...Added"
            return render(request,"addblogs.html", {'msg': msg})
        else:
            msg="plz fill the entries correctly"
            return render(request,"addblogs.html", {'msg': msg})