from blog_app.models import ArticleModel
from django.shortcuts import render

def recent_article(request):
    articles = ArticleModel.objects.all()[:3]
    return {'recents_articles': articles}