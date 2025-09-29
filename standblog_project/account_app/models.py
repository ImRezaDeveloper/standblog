from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    father_s_name = models.CharField(max_length=30)
    melicode = models.IntegerField(max_length=20)
    image = models.ImageField(upload_to='profiles/image', null=True, blank=True)
    
    def __str__(self):
        return self.user.username