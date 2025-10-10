from django.shortcuts import render, get_object_or_404
from .models import ArticleModel, Category
from django.core.paginator import Paginator

# Create your views here.

def post_detail(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    return render(request, 'blog_app/post-details.html', {'article': article})

def article_list(request):
    articles = ArticleModel.objects.all()
    
    # paginator
    page = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page)
    return render(request, 'blog_app/article_list.html', {'articles': object_list})

def categories_articles(request, pk):
    categories = get_object_or_404(Category, id=pk)
    articles = categories.article_category.all()

    return render(request, 'blog_app/article_list.html', {'articles': articles})