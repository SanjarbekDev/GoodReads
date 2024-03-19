
from django.contrib import admin
from django.urls import path, include
from .views import LandingPageView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', LandingPageView.as_view(), name='home'),
    path("admin/", admin.site.urls),
    # costom url
    path('users/',include('users.urls')),
    path('books/',include('books.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
