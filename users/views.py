from django.shortcuts import redirect, render
from django.views import View
from . forms import UserCreateForms, UserUpdateForm
from users.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import login, logout
from django.contrib import messages
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
            messages.success(request, "Logged in")
            return redirect("books:book_list")
        else:
            return render(request, 'users/login.html', {'login_form': form})
        
class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You sucsessfully logged out ...')
        return redirect('home')
        

class ProfileViev(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        # if not user.is_authenticated:
        #     return redirect('users:login')
        return render(request, 'users/profile.html', {'user' : user})


class ProfileUpdateView(LoginRequiredMixin ,View):
    def get(self, request):
        user_update_form = UserUpdateForm(instance=request.user)
        return render(request, 'users/profile_edit.html',{'form' : user_update_form})
    
    def post(self, request):
        user_update_data = UserUpdateForm(instance=request.user, 
                                          data=request.POST,
                                          files=request.FILES
        )

        if user_update_data.is_valid():
            user_update_data.save()
            messages.success(request , "Profile succsessfuly changes!")
            return redirect('users:profile')
        
        return render(request , "users/profile_edit.html", {'form':user_update_data})