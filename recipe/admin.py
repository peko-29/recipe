from django.contrib import admin
from .models import Menu, Genre, Small_Genre, Material, Menu_Material

# Register your models here.
admin.site.register(Menu)
admin.site.register(Genre)
admin.site.register(Small_Genre)
admin.site.register(Material)
admin.site.register(Menu_Material)