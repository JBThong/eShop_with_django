from django.contrib import admin
from django.urls import path
from .views import Home, SignUp, SignIn, signout

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('signup', SignUp.as_view(), name='signup'),
    path('login', SignIn.as_view(), name='login'),
    path('logout', signout, name='logout'),
]