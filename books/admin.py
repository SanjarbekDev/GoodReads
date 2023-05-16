from django.contrib import admin
from .models import Book, Author, BookAuthor, BookReview
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'isbn')
    list_display = ('title', 'isbn', 'description')
    # list_filter = ()

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'bio',)

class ReviewAdmin(admin.ModelAdmin):
    pass

class BookAuthorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(BookReview, ReviewAdmin)
admin.site.register(BookAuthor, BookAuthorAdmin)
