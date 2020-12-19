from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from django.views import View

from mystore.models import Product, Order, User, OrderDetail

class Orders(View):
    def get(self, request):
        user = request.session.get('user')
        orders = Order.get_orders_by_user(user)
        return render(request, 'orders.html', {'orders': orders})

class OrderDetailV(View):
    def get(self, request, id):
        orders_detail = OrderDetail.get_order_detail_by_order(id)
        return render(request, 'order_detail.html', {'products': orders_detail})