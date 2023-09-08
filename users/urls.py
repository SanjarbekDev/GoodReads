from django.urls import path
from .views import Registration, Login


app_name = "users"

urlpatterns = [
    path('signup/', Registration.as_view(), name = 'register'),
    path('signin/', Login.as_view(), name = 'login')
]