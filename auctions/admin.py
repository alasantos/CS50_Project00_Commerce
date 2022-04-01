from django.contrib import admin

from auctions.models import Category, Item

# Register your models here.

admin.site.register( Category)
admin.site.register( Item )