from django.db import models

# Create your models here.

class ArticleModel(models.Model):
    
    title = models.CharField(max_length=40)
    body = models.TextField()
    image = models.ImageField(upload_to='media/blogs', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title