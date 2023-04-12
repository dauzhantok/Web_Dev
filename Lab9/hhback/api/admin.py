from django.contrib import admin
from models import Company, Vacancy


@admin.register(Company)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Vacancy)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'salary', 'company')