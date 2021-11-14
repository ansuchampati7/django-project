from django import urls
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.myblogs),
    path("addblogs/", views.addblogs),
    path("submit/", views.submit.as_view())

]