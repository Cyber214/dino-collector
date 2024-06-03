# We're already importing render from django.shortcuts
from django.shortcuts import render

...

def about(request):
  return render(request, 'about.html')