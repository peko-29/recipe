from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length = 100)
    cost = models.IntegerField()
    time = models.IntegerField()
    process = models.TextField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbohydrate = models.FloatField()
    cal = models.FloatField()
    img = models.ImageField()
    
