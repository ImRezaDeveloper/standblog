from blog_app.models import ArticleModel, Category
from django.shortcuts import render

def recent_article(request):
    articles = ArticleModel.objects.all()[:3]
    categories = Category.objects.all()
    return {'recents_articles': articles, 'categories': categories}