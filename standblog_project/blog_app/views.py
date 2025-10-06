from django.shortcuts import render, get_object_or_404
from .models import ArticleModel

# Create your views here.

def post_detail(request, slug):
    article = get_object_or_404(ArticleModel, slug=slug)
    return render(request, 'blog_app/post-details.html', {'article': article})
