from django.db import models
from django.urls import reverse

# Create your models here.
class Squishmallow(models.Model):
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    squad = models.CharField(max_length=100)
    squish_date = models.DateField(auto_now=False)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'squish_id': self.id})








