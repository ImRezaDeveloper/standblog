from django.contrib import admin
from .models import ArticleModel, Category

# Register your models here.

admin.site.register(ArticleModel)
admin.site.register(Category)