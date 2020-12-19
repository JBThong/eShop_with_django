from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password
from django.views import View

from mystore.models import Product, Order, User, OrderDetail

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        user = request.session.get('user')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        print(address, phone, user, cart)

        order = Order(user=User(id=user), address=address, phone=phone)
        order.save()
        for product in products:
            quantity = cart.get(str(product.id))
            order_detail = OrderDetail(order=Order(id=order.id),
                                       product=Product(id=product.id),
                                       quantity=quantity,
                                       price=product.price)
            order_detail.save()
        request.session['cart'] = {}
        return redirect('cart')
