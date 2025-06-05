from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=30)
    ingredients = models.CharField()
    preparation_time = models.CharField()
    instructions = models.TextField()
    
    def __str__(self):
        return self.title
