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
    
    def __str__(self):
        return self.name
    
class Genre(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
    
class Small_Genre(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Material(models.Model):
    small_genre = models.ForeignKey(Small_Genre, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name
        
class Menu_Material(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    amount = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.amount