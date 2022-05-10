from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Squishmallow


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
    return render(request, 'squishes/detail.html', {'squish': squish})

class SquishCreate(CreateView):
    model = Squishmallow
    fields = '__all__'

class SquishUpdate(UpdateView):
    model = Squishmallow
    fields = '__all__'

class SquishDelete(DeleteView):
    model = Squishmallow
    success_url = '/squishes/'




