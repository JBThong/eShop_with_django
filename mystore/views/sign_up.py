from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.views import View
from mystore.utils import validation_phone, validate_email

from mystore.models import User


class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        # validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        error_message = None

        user = User(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password)
        error_message = self.validateCustomer(user)

        if not error_message:
            print(first_name, last_name, phone, email, password)
            user.password = make_password(user.password)
            user.register()
            return redirect('homepage')
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self, customer):
        error_message = None;
        if (not validation_phone(customer.phone)):
            error_message = 'Phone Number is not in format'
        elif not validate_email(customer.email):
            error_message = 'Email is not in format'
        elif customer.isExists():
            error_message = 'Email Address Already Registered..'

        return error_message