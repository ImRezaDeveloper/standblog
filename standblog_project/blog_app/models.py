from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
    
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
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_article', null=True, blank=True, verbose_name='نویسنده')
    title = models.CharField(max_length=40, verbose_name='عنوان')
    category = models.ManyToManyField(Category, related_name='article_category', verbose_name='دسته بندی')
    body = models.TextField(help_text='Enter a valid body because important!', verbose_name='بدنه')
    image = models.ImageField(upload_to='media/blogs', null=True, blank=True, verbose_name='عکس')
    created = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    updated = models.DateTimeField(auto_now=True, verbose_name='تاریخ آپدیت')
    # custom queryset
    objects = models.Manager()
    custom_query = ArticleManager()
    slug = models.SlugField(max_length=100, null=True, blank=True, verbose_name='اسلاگ')
    
    class Meta:
        ordering = ('-created',)
    
    def save(self):
        self.slug = slugify(self.title)
        super().save()
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'

# Comments
class Comment(models.Model):
    article = models.ForeignKey(ArticleModel, on_delete=models.CASCADE, related_name='article_comment', verbose_name='مقاله')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    name = models.CharField(max_length=50, null=True, blank=True, verbose_name='اسم')
    body = models.TextField(max_length=300, null=True, blank=True, verbose_name='بدنه')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies', verbose_name='والد')
    
    def __str__(self):
        return self.body[:20]
    
    class Meta:
        verbose_name='نظر'
        verbose_name_plural='نظرات'
    
# ContactUs
class ContactUs(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    text = models.CharField(max_length=100, verbose_name='موضوع')
    email = models.EmailField(verbose_name='آدرس ایمیل')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ انتشار')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='ارتباط با ما'
        verbose_name_plural='ارتباطات'