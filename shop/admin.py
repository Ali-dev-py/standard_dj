from django.contrib import admin
from django.db import models

from .models import Product, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    #prepopulated_fields = {'slug':('name',)}
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug':('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'updated']
    list_filter = ['created', 'updated']

    #prepopulated_fields = {'slug':('name',)}
    
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug':('name',)}