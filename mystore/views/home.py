from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from mystore.models.product import Product
from mystore.models.category import Category
from django.views import View


# Create your views here.
class Home(View):
    def get(self, request, *args, **kwargs):
        products = None
        categories = Category.get_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products();

        data = {}
        data['products'] = products
        data['categories'] = categories

        print('you are : ', request.session.get('email'))
        return render(request, 'home.html', data)
