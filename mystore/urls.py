from django.contrib import admin
from django.urls import path
from .views import Home, SignUp

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('signup', SignUp.as_view(), name='signup'),
    # path('login', Login.as_view(), name='login'),
    # path('logout', logout , name='logout'),
]