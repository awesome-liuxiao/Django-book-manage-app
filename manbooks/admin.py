from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Book name',           {'fields': ['book_name']}),
        ('Book author',         {'fields': ['author_name']}),
        ('Publication year',    {'fields': ['pub_year']}),
        ('Link address',        {'fields': ['link_addr']}),
    ]
admin.site.register(Book)
