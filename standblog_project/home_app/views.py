from django.shortcuts import render
from blog_app.models import ArticleModel, Category

# Create your views here.

def home(request):
    articles = ArticleModel.objects.all()
    categories = Category.objects.all()
    return render(request, 'home_app/index.html', {'articles': articles, 'category': categories})