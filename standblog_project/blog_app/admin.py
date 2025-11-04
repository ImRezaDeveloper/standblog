from django.contrib import admin
from .models import ArticleModel, Category, Comment, ContactUs, Like

# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display = ("title", 'author')
    prepopulated_fields = {"slug": ("title",)}
    # list_editable = ('image',)
    list_filter = ('created',)
    search_fields = ('title', 'body')
    
admin.site.register(ArticleModel, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(ContactUs)
admin.site.register(Like)
