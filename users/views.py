from django.shortcuts import redirect, render
from django.views import View
from . forms import UserCreateForms, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import login

# Create your views here.


class Registration(View):
    def get(self, request):
        forms = UserCreateForms()
        context = {
            'form' : forms,
        }
        return render(request, 'users/register.html', context)
    
    def post(self, request):
        create_form = UserCreateForms(data=request.POST)
        
        if create_form.is_valid():
            create_form.save()

            return redirect('users:login')
        else:
            context = {
                'form' : create_form,
            }
            return render(request, 'users/register.html', context)


class Login(View):

    def get(self, request):
        forms = AuthenticationForm()
        return render(request, 'users/login.html', {'login_form': forms})
    
    def post(self, request):
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            # logged in the user
            user  = form.get_user()
            login(request, user)

            return redirect('landing_page')
        else:
            return render(request, 'users/login.html', {'login_form': form})




    