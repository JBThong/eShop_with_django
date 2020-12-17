from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from mystore.models.product import Product
from mystore.models.category import Category
from django.views import View


# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        products = Product.get_all_products()
        # return HttpResponse('Hello, World!')

        return render(request, 'home.html', {'products': products})