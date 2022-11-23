from django.contrib import admin

from core.models import BookLoan, Book, Author, Partner, Category

# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Partner)
admin.site.register(Category)
admin.site.register(BookLoan)