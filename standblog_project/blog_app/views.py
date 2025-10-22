from django.shortcuts import redirect, render, get_object_or_404
from .models import ArticleModel, Category, Comment, ContactUs
from django.core.paginator import Paginator
from .forms import ContactUsForms
from django.db.models import Count
from django.views.generic.base import TemplateView, RedirectView
# from django.views.generic.list import Crea
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy

# Create your views here.

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
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            email = form.cleaned_data['email']
            ContactUs.objects.create(title=title, text=text, email=email)
            return redirect('home')
    else:
        form = ContactUsForms()
    return render(request, 'blog_app/contact_us.html', {'form': form})

# class ArticleList(ListView):
#     queryset = ArticleModel.objects.all()
#     template_name = 'blog_app/article_list.html'
    
#     def get(self, request):
#         page = request.GET.get('page')
#         paginator = Paginator(self.queryset, 1)
#         object_list = paginator.get_page(page)
#         return render(request, self.template_name, {'articles': object_list})

class ArticleList(TemplateView):
    
    template_name = 'blog_app/article_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['articles'] = ArticleModel.objects.all()
        return context
    
class HomePageRedirectView(RedirectView):
    # url = '/'
    pattern_name = 'home'
    
class ArticleDetail(DetailView):
    model = ArticleModel
    template_name = 'blog_app/post-details.html'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = ArticleModel.objects.get(slug=self.kwargs['slug'])
        return queryset
    
    def get_context_data(self, **kwargs,):
        context = super().get_context_data(**kwargs)
        context["article"] = ArticleModel.objects.get(slug=self.kwargs['slug'])
        return context
    
    def post(self, request):
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(body=body, article=self.queryset, user=request.user, parent_id=parent_id)
        
class ContactUsView(FormView):
    template_name = 'blog_app/contact_us.html'
    form_class = ContactUsForms
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form = form.cleaned_data
        ContactUs.objects.create(**form)
        return super().form_valid(form)

class MessageView(CreateView):
    model = ContactUs
    fields = ('title', 'text')
    success_url = reverse_lazy('home')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['messages'] = ContactUs.objects.all()
        return context
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.email = self.request.user.email
        instance.save()
        return super().form_valid(form)
        