from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ArticleModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_article', null=True, blank=True, unique=True)
    title = models.CharField(max_length=40)
    body = models.TextField(help_text='Enter a valid body because important!')
    image = models.ImageField(upload_to='media/blogs', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title