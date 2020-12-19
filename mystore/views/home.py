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

    def post(self, request):
        product_id = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(product_id)
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product_id)
                    else:
                        cart[product_id] = quantity - 1
                else:
                    if Product.get_products_by_id(product_id).get().stock - cart[product_id] > 0:
                        cart[product_id] = quantity + 1
                    else:
                        print('Product out of stock')

            else:
                cart[product_id] = 1
        else:
            cart={}
            if Product.get_products_by_id(product_id).get().stock > 0:
                cart[product_id] = 1
            else:
                print('Product out of stock')

        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('homepage')
