# blog_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('article/<slug:slug>/', views.post_detail, name='single-article'),
    path('articles/list', views.article_list, name='articles'),
    path('category/<int:pk>', views.categories_articles, name='category_article'),
    path('search/', views.search_article, name='search_article'),
    path('contact-us/', views.contact_us, name='contact_us')
]
