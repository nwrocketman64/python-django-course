from django.contrib import admin

from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # prepopulated_fields = {"slug": ("title",)}
    pass

admin.site.register(Book, BookAdmin)