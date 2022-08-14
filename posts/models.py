from django.db import models

# Create your models here.


class postModel(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=5000)
    
    def __str__(self) -> str:
        return self.name