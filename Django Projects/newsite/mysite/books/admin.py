from django.contrib import admin
from .models import book

# Register your models here.

#To make the book table show on admin panel
admin.site.register(book)
