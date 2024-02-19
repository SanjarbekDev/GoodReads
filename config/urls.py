
from django.contrib import admin
from django.urls import path, include
from .views import LandingPageView

urlpatterns = [
    path('', LandingPageView.as_view(), name='home'),
    path("admin/", admin.site.urls),
    # costom url
    path('users/',include('users.urls')),
    path('books/',include('books.urls')),
]
