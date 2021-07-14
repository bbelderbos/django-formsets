from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'authors', 'description',
                    'image_link', 'inserted')
    search_fields = ('title', 'authors', 'description')


admin.site.register(Book, BookAdmin)
