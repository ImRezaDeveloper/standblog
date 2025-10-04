from django.contrib import admin
from .models import ArticleModel, Category

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    
admin.site.register(ArticleModel, ArticleAdmin)
admin.site.register(Category)