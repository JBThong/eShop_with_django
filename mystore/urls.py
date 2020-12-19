from django.contrib import admin
from django.urls import path
from .views import Home, SignUp, SignIn, signout, Cart, CheckOut, Orders, OrderDetailV, CancelOrdel
from .middlewares import auth_middleware

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('signup', SignUp.as_view(), name='signup'),
    path('login', SignIn.as_view(), name='login'),
    path('logout', signout, name='logout'),
    path('cart', Cart.as_view(), name='cart'),
    path('check-out', auth_middleware(CheckOut.as_view()), name='checkout'),
    # path('check-out', CheckOut.as_view(), name='checkout'),
    path('orders', auth_middleware(Orders.as_view()), name='orders'),
    path('orders/<int:id>', OrderDetailV.as_view(), name='order_detail'),
    path('orders/cancel/<int:id>', CancelOrdel.as_view(), name='update_order'),

]