from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class postModel(models.Model):
    auther = models.ForeignKey(User ,on_delete=models.CASCADE, related_name='user_post  ')
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    img = models.ImageField(upload_to='posts/')
    
    def __str__(self) -> str:
        return self.name