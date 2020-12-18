from django.shortcuts import render
from django.views import View

from mystore.models import Product


class Cart(View):
    def get(self, request):
        carts = request.session.get('cart')
        if carts:
            ids = list(carts.keys())
            products = Product.get_products_by_id(ids)
            # print(products.name)
        return render(request, 'cart.html', {'products': products})

