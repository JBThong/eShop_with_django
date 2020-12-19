from django.shortcuts import render, redirect, HttpResponseRedirect

from django.contrib.auth.hashers import check_password
from mystore.models.user import User
from django.views import View


class SignIn(View):
    return_url = None
    def get(self , request):
        self.return_url = request.GET.get('return_url')
        return render(request, 'login.html')

    def post(self , request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.get_user_by_email(email)
        error_message = None
        if user:
            flag = check_password(password, user.password)
            if flag:
                request.session['user'] = user.id

                if self.return_url:
                    return HttpResponseRedirect(self.return_url)
                else:
                    self.return_url = None
                    return redirect('homepage')
            else:
                error_message = 'Email or Password invalid !!'
        else:
            error_message = 'Email or Password invalid !!'

        return render(request, 'login.html', {'error': error_message})

def signout(request):
    request.session.clear()
    return redirect('homepage')
