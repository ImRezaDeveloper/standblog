from django.shortcuts import render
from blog_app.models import ArticleModel

# Create your views here.

def home(request):
    articles = ArticleModel.objects.all()
    return render(request, 'home_app/index.html', {'articles': articles})