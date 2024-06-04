from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('dinos/', views.dino_index, name='dino-index'),
  path('dinos/<int:dino_id>/', views.dino_detail, name='dino-detail'),
  path('dinos/create/', views.DinoCreate.as_view(), name='dino-create'),
]