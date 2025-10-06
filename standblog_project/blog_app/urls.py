# blog_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('article/<slug:slug>/', views.post_detail, name='single-article'),
]
