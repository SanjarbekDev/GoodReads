from django.urls import path
from .views import Registration, Login, ProfileViev, LogoutView


app_name = "users"

urlpatterns = [
    path('signup/', Registration.as_view(), name = 'register'),
    path('signin/', Login.as_view(), name = 'login'),
    path('profile/', ProfileViev.as_view(), name='profile'),
    path('logout/', LogoutView.as_view(), name='logout'),
]