from django.urls import path
from . import views

urlpatterns = [
    path('article/<int:pk>', views.post_detail, name='single-article')
]
