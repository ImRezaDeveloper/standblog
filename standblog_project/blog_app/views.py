from django.shortcuts import redirect, render, get_object_or_404
from .models import ArticleModel, Category, Comment
from django.core.paginator import Paginator
from .forms import ContactUsForms
from django.db.models import Count

# Create your views here.

def post_detail(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=article, user=request.user, parent_id=parent_id)
    
    return render(request, 'blog_app/post-details.html', {
        'article': article
    })


def article_list(request):
    articles = ArticleModel.objects.annotate(comment_count=Count('article_comment'))

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

def contact_us(request):
    if request.method == 'POST':
        form = ContactUsForms(request.POST)   
        if form.is_valid():
            print(form.cleaned_data['name'])
            return redirect('home')
    else:
        form = ContactUsForms()
    return render(request, 'blog_app/contact_us.html', {'form': form})