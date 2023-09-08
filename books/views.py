from django.views import View
from django.shortcuts import render
from .models import Book
# Create your views here.

class BookListview(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/books.html",{'books':books})
    

class BookDetialView(View):
    def get(self, request):
        pass