from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('data-list/', views.dataList, name="data-list"),
]