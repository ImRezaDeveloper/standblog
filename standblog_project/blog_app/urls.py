# blog_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('article/<slug:slug>/', views.ArticleDetail.as_view(), name='single-article'),
    path('articles/list', views.ArticleList.as_view(), name='articles'),
    path('category/<int:pk>', views.categories_articles, name='category_article'),
    path('search/', views.search_article, name='search_article'),
    path('contact-us/', views.ContactUsView.as_view(), name='contact_us'),
    path('contact-us/<int:pk>', views.MessageUpdateView.as_view(), name='contact_us'),
    path('contact-us/delete/<int:pk>', views.MessageDeleteView.as_view(), name='message_delete'),
    path('redirect', views.HomePageRedirectView.as_view(), name='redirect'),
    path('article/<slug:slug>/like/', views.likeArticle, name='article_like'),
]
