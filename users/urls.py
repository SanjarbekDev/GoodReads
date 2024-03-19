from django.urls import path
from .views import Registration, Login, ProfileViev, LogoutView, ProfileUpdateView


app_name = "users"

urlpatterns = [
    path('signup/', Registration.as_view(), name = 'register'),
    path('signin/', Login.as_view(), name = 'login'),
    path('profile/', ProfileViev.as_view(), name='profile'),
    path('profile/edit/', ProfileUpdateView.as_view(), name="profile_edit"),
    path('logout/', LogoutView.as_view(), name='logout'),
]