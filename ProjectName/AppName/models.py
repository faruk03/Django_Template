from django.db import models

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='media')
    
    def __str__(self):
        return self.name

