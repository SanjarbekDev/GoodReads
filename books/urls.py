from django.urls import path, include
from .views import BookListview, BookDetialView

urlpatterns = [
    path('',BookListview.as_view(), name='landing_page'),
    path('/<int:id>/',BookDetialView.as_view(), name='detial'),
    path('users/', include('users.urls')),
]