from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from .models import Dino
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(LoginView):
  template_name = 'home.html'

def about(request):
  return render(request, 'about.html')

@login_required
def dino_index(request):
  dinos = Dino.objects.filter(user=request.user)
  # You could also retrieve the logged in user's dinos like this
  # dinos = request.user.dino_set.all()
  return render(request, 'dinos/index.html', { 'dinos': dinos })

def dino_detail(request, dino_id):
  dino = Dino.objects.get(id=dino_id)
  return render(request, 'dinos/detail.html', { 'dino': dino })

class DinoCreate(LoginRequiredMixin, CreateView):
  model = Dino
  fields = ['name', 'breed', 'description', 'age']
  # This inherited method is called when a
  # valid dino form is being submitted
  def form_valid(self, form):
    # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user  # form.instance is the dino
    # Let the CreateView do its job as usual
    return super().form_valid(form)

class DinoUpdate(LoginRequiredMixin, UpdateView):
  model = Dino
  fields = ['species', 'description', 'age']

class DinoDelete(LoginRequiredMixin, DeleteView):
  model = Dino
  success_url = '/dinos/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in
      login(request, user)
      return redirect('dino-index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'signup.html', context)
  # Same as: return render(request, 'signup.html', {'form': form, 'error_message': error_message})