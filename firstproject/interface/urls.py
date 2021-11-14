from django import urls
from django.urls import path, include
from . import views


urlpatterns = [
    path("", views.homei),
    path("logini/", views.logini),
    path("signin/", views.signin),
    path("signin/aftersignin/", views.aftersignin),
    path("logini/afterlogin/", views.afterlogin),
    path("logout/", views.logout),
    path("user/", include("authentication.urls")),
    
]