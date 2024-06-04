# We're already importing render from django.shortcuts
from django.shortcuts import render
from .models import Dino


# Views
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def dino_index(request):
  dinos = Dino.objects.all()
  return render(request, 'dinos/index.html', { 'dinos': dinos })

def dino_detail(request, dino_id):
  dino = Dino.objects.get(id=dino_id)
  return render(request, 'dinos/detail.html', { 'dino': dino })