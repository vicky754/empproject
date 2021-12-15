
from django.urls import path
from .views import *
from app1.middlewares.login_required_middleware import login_required
from app1.middlewares.cannot_access_after_login import cannotAaccessAfterLogin

urlpatterns = [
    
    path('',login_required(home),name='home'),
    path('login/',cannotAaccessAfterLogin(login),name='login'),
    path('signup/',cannotAaccessAfterLogin(signup)),
    path('logout/',login_required(signout),name='logout'),
]   