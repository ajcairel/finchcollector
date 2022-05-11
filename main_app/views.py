from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Squishmallow, Squad
from .forms import StyleForm


# Create your views here.
# Add the Cat class & list and view function below the imports


def home(request):
    # return HttpResponse('<h1> Squish Boi </h1> <li><a href="/about">About</a></li><li><a href="/squishes">View All My Squishes</a></li>')
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')

def squishes_index(request):
    squishes = Squishmallow.objects.all()
    return render(request, 'squishes/index.html', {'squishes': squishes })

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

class SquishCreate(CreateView):
    model = Squishmallow
    fields = '__all__'

class SquishUpdate(UpdateView):
    model = Squishmallow
    fields = ['squish_date']

class SquishDelete(DeleteView):
    model = Squishmallow
    success_url = '/squishes/'

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

def assoc_squad(request, squish_id, squad_id):
  # Assoc toy with the cat
  Squishmallow.objects.get(id=squish_id).squads.add(squad_id)
  return redirect('detail', squish_id=squish_id)

def unassoc_squad(request, squish_id, squad_id):
  # Assoc toy with the cat
  Squishmallow.objects.get(id=squish_id).squads.remove(squad_id)
  return redirect('detail', squish_id=squish_id)





class SquadList(ListView):
  model = Squad

class SquadDetail(DetailView):
  model = Squad

class SquadCreate(CreateView):
  model = Squad
  fields = '__all__'

class SquadUpdate(UpdateView):
  model = Squad
  fields = '__all__'

class SquadDelete(DeleteView):
  model = Squad
  success_url = '/squishes/'


