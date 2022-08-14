from distutils.command.upload import upload
from django.db import models

# Create your models here.


class postModel(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    img = models.ImageField(upload_to='posts/')
    
    def __str__(self) -> str:
        return self.name