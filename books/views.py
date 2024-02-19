from django.views import View
from django.shortcuts import render
from .models import Book
# Create your views here.

class BookListview(View):
    def get(self, request):
        books = Book.objects.all()
        return render(request, "books/books.html",{'books':books})
    

class BookDetialView(View):
    def get(self, request, id):
        book = Book.objects.get(id=id)
        context = {
            'book' : book
        }
        return render(request, "books/detial.html", context)