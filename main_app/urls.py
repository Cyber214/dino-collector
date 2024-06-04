from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('dinos/', views.dino_index, name='dino-index'),
  path('dinos/<int:dino_id>/', views.dino_detail, name='dino-detail'),
  path('dinos/create/', views.DinoCreate.as_view(), name='dino-create'),
  path('dinos/<int:pk>/update/', views.DinoUpdate.as_view(), name='dino-update'),
  path('dinos/<int:pk>/delete/', views.DinoDelete.as_view(), name='dino-delete'),
  path('accounts/signup/', views.signup, name='signup'),
]