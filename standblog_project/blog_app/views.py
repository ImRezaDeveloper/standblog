from django.shortcuts import render, get_object_or_404
from .models import ArticleModel, Category, Comment, Reply_Comment
from django.core.paginator import Paginator

# Create your views here.

def post_detail(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    reply_comments = Reply_Comment.objects.all()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        body = request.POST.get('body')
        
        Comment.objects.create(article=article, user=name, name=name, body=body)
    comments = article.article_comment.all()
    return render(request, 'blog_app/post-details.html', {'article': article, 'comments': comments})

def article_list(request):
    articles = ArticleModel.objects.all()
    
    # paginator
    page = request.GET.get('page')
    paginator = Paginator(articles, 1)
    object_list = paginator.get_page(page)
    return render(request, 'blog_app/article_list.html', {'articles': object_list})

def categories_articles(request, pk):
    categories = get_object_or_404(Category, id=pk)
    articles = categories.article_category.all()

    return render(request, 'blog_app/article_list.html', {'articles': articles})

def search_article(request):
    q = request.GET.get('q', '')
    articles = ArticleModel.objects.filter(title__icontains=q)
    page = request.GET.get('page')
    paginator = Paginator(articles, 1)
    object_list = paginator.get_page(page)
    return render(request,'blog_app/article_list.html', {'articles': object_list, 'q': q})