# We're already importing render from django.shortcuts
from django.shortcuts import render

class Dino:
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

dinosaurs = [
  Dino('Troy', 'Tyrannosaurus', 'The king of dinosaurs.', 8),
  Dino('Tina', 'Triceratops', 'Known for its three horns.', 5),
  Dino('Vicky', 'Velociraptor', 'Swift and intelligent predator.', 3),
  Dino('Stella', 'Stegosaurus', 'Characterized by its bony plates and tail spikes.', 10)
]

def about(request):
  return render(request, 'about.html')

def dino_index(request):
  return render(request, 'dinos/index.html', { 'dinos': dinosaurs })