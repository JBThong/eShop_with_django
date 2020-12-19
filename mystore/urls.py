from django.contrib import admin
from django.urls import path
from .views import Home, SignUp, SignIn, signout, Cart, CheckOut
from .middlewares import auth_middleware

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('signup', SignUp.as_view(), name='signup'),
    path('login', SignIn.as_view(), name='login'),
    path('logout', signout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', auth_middleware(CheckOut.as_view()) , name='checkout'),
]