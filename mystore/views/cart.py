from django.shortcuts import render
from django.views import View

from mystore.models import Product


class Cart(View):
    def get(self, request):
        carts = request.session.get('cart')
        products = None
        is_has_product = False
        if carts:
            ids = list(carts.keys())
            products = Product.get_products_by_id(ids)
        if products:
            is_has_product = True
        return render(request, 'cart.html', {'products': products, 'is_has_product': is_has_product})

