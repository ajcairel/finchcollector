from django.shortcuts import render
from django.http import HttpResponse 

# Create your views here.
# Add the Cat class & list and view function below the imports
class Finch:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, science, habitat, behavior):
    self.name = name
    self.science = science
    self.habitat = habitat
    self.behavior = behavior

finches = [
    Finch('American Goldfinch', 'Spinus tristis', 'Open Woodlands', 'Foliage Gleaner'),
    Finch('Black Rosy-Finch', 'Leucosticte atrata', 'Tundra', 'Ground Forager'),
    Finch('Blue Grosbeak', 'Passerina caerulea', 'Open Woodlands', 'Foliage Gleaner'),
    Finch('Cassia Crossbill', 'Loxia sinesciuris', 'Forests', 'Foliage Gleaner'),
    Finch('Northern Cardinal', 'Cardinalis cardinalis', 'Open Woodlands', 'Ground Forager')
]

def home(request):
    return HttpResponse('<h1> Binch Boi </h1>')

def about(request):
    return render(request, 'about.html')
