from django.db import models

# Create your models here.
class Squishmallow(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    squad = models.CharField(max_length=100)
    squish_date = models.DateField(auto_now=False)








