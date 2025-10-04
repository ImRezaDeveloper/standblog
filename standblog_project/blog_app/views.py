from django.shortcuts import render, get_object_or_404
from .models import ArticleModel

# Create your views here.

def post_detail(request, pk):
    article = get_object_or_404(ArticleModel, id=pk)
    return render(request, 'blog_app/post-details.html', {'article': article})
