# We're already importing render from django.shortcuts
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
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

class DinoCreate(CreateView):
  model = Dino
  fields = ['name', 'breed', 'description', 'age']
  success_url = '/dinos/'

class DinoUpdate(UpdateView):
  model = Dino
  fields = ['breed', 'description', 'age']

class DinoDelete(DeleteView):
  model = Dino
  success_url = '/dinos/'
