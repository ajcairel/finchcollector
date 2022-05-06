from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
# Add the Cat class & list and view function below the imports
class Squishmallow:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, size, squad):
    self.name = name
    self.size = size
    self.squad = squad
  

squishes = [
    Squishmallow('Harrison the Dog', '7.5" Hug Me', 'None'),
    Squishmallow('Candess The Cow', '8"', 'None'),
    Squishmallow('Bop The Bunny', '16"', 'Easter'),
    Squishmallow('Malcom the Mushroom', '16"', 'None'),
    Squishmallow('Gary the Giraffe', '7"', 'None'),
    Squishmallow('Avery the Mallard', '5"', 'Farm'),
  
   
]

def home(request):
    return HttpResponse('<h1> Squish Boi </h1> <li><a href="/about">About</a></li><li><a href="/squishes">View All My Squishes</a></li>')

def about(request):
    return render(request, 'about.html')

def squishes_index(request):
    return render(request, 'squishes/index.html', {'squishes': squishes })


