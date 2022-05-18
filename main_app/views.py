from django.shortcuts import render, redirect
import os
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Squishmallow, Squad
from .forms import StyleForm


# Create your views here.
# Add the Cat class & list and view function below the imports


def home(request):
    # return HttpResponse('<h1> Squish Boi </h1> <li><a href="/about">About</a></li><li><a href="/squishes">View All My Squishes</a></li>')
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

@login_required
def squishes_index(request):
    # squishes = Squishmallow.objects.all() # This will show all squishes across the board
    squishes = request.user.squishmallow_set.all()
    # squishes = Squishmallow.objects.filter(user=request.user) # This does the same as above
    return render(request, 'squishes/index.html', {'squishes': squishes })

@login_required
def squishes_detail(request, squish_id):
    squish = Squishmallow.objects.get(id=squish_id)
    # Get the squads that the squishmallow doesn't have
    # First, get a list of ids of squads that the squishmallow does have
    id_list = squish.squads.all().values_list('id')
    squads_squish_does_not_have = Squad.objects.exclude(id__in=id_list)
    size_form = StyleForm()
    return render(request, 'squishes/detail.html', {
        'squish': squish,
        'size_form': size_form,
        'squads': squads_squish_does_not_have
        })

class SquishCreate(LoginRequiredMixin, CreateView):
    model = Squishmallow
    fields = ['name', 'squish_date']
    # This inherited method is called when a
  # valid cat form is being submitted
    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
      form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
      return super().form_valid(form)

class SquishUpdate(LoginRequiredMixin, UpdateView):
    model = Squishmallow
    fields = ['squish_date']

class SquishDelete(DeleteView):
    model = Squishmallow
    success_url = '/squishes/'

@login_required
def add_size(request, squish_id):
  # create a ModelForm instance using the data in request.POST
  form = StyleForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_style = form.save(commit=False)
    new_style.squishmallow_id = squish_id
    new_style.save()
  return redirect('detail', squish_id=squish_id)

@login_required
def assoc_squad(request, squish_id, squad_id):
  # Assoc toy with the cat
  Squishmallow.objects.get(id=squish_id).squads.add(squad_id)
  return redirect('detail', squish_id=squish_id)

@login_required
def unassoc_squad(request, squish_id, squad_id):
  # Assoc toy with the cat
  Squishmallow.objects.get(id=squish_id).squads.remove(squad_id)
  return redirect('detail', squish_id=squish_id)





class SquadList(LoginRequiredMixin, ListView):
  model = Squad

class SquadDetail(LoginRequiredMixin, DetailView):
  model = Squad

class SquadCreate(LoginRequiredMixin, CreateView):
  model = Squad
  fields = '__all__'

class SquadUpdate(LoginRequiredMixin, UpdateView):
  model = Squad
  fields = '__all__'

class SquadDelete(LoginRequiredMixin, DeleteView):
  model = Squad
  success_url = '/squishes/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


