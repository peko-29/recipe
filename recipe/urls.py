from django.urls import path
from . import views
app_name= 'recipe'

urlpatterns = [
    path("", views.index, name="index"),
    path('detail/<int:menu_id>/', views.detail, name='detail'),
]