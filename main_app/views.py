from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Squishmallow
from .forms import StyleForm


# Create your views here.
# Add the Cat class & list and view function below the imports


def home(request):
    return HttpResponse('<h1> Squish Boi </h1> <li><a href="/about">About</a></li><li><a href="/squishes">View All My Squishes</a></li>')

def about(request):
    return render(request, 'about.html')

def squishes_index(request):
    squishes = Squishmallow.objects.all()
    return render(request, 'squishes/index.html', {'squishes': squishes })

def squishes_detail(request, squish_id):
    squish = Squishmallow.objects.get(id=squish_id)
    size_form = StyleForm()
    return render(request, 'squishes/detail.html', {
        'squish': squish,
        'size_form': size_form
        })

class SquishCreate(CreateView):
    model = Squishmallow
    fields = '__all__'

class SquishUpdate(UpdateView):
    model = Squishmallow
    fields = '__all__'

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




