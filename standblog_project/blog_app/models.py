from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
# build custom queryset
class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())
    
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(title='Blog')
    
class ArticleModel(models.Model):
    # CHOISES = (
    #     ('A', 'Python'),
    #     ('B', 'Django')
    # )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_article', null=True, blank=True, unique=True)
    title = models.CharField(max_length=40)
    category = models.ManyToManyField(Category, related_name='article_category')
    body = models.TextField(help_text='Enter a valid body because important!')
    image = models.ImageField(upload_to='media/blogs', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    # custom queryset
    objects = models.Manager()
    custom_query = ArticleManager()
    
    def __str__(self):
        return self.title