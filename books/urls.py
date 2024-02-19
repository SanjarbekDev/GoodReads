from django.urls import path, include
from .views import BookListview, BookDetialView

app_name = "books"
urlpatterns = [
    path('',BookListview.as_view(), name='book_list'),
    path('<int:id>/',BookDetialView.as_view(), name="detial"),
    path('users/', include('users.urls')),
]