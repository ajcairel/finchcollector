from django.db import models
from django.urls import reverse

KIND = (
    ('3.5', '3.5" Clip On'),
    ('5', '5"'),
    ('6', '6"'),
    ('7', '7"'),
    ('7.5', '7.5"'),
    ('8', '8"'),
    ('10', '10"'),
    ('12', '12"'),
    ('14', '14"'),
    ('16', '16"'),
    ('20', '20"'),
    ('24', '24"'),
    ('H', 'Hug Mee'),
    ('S', 'Stackable'),
    ('F', 'Flip-A-Mallow'),
)
# Create your models here.
class Squad(models.Model):
  name = models.CharField(max_length=50)
  # Squads have a M:M related manager named
  # squishmallow_set

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('squads_detail', kwargs={'pk': self.id})


class Squishmallow(models.Model):
    name = models.CharField(max_length=100)
    #size = models.IntegerField()
    #squad = models.CharField(max_length=100)
    squish_date = models.DateField(auto_now=False)
    squads = models.ManyToManyField(Squad)

    def __str__(self):
        return f'{self.name} ({self.id})'

    def get_absolute_url(self):
        return reverse('detail', kwargs={'squish_id': self.id})

class Style(models.Model):
    size = models.CharField(
        max_length=4,
        choices=KIND
    )
    squishmallow = models.ForeignKey(Squishmallow, on_delete=models.CASCADE)

    def __str__(self):
        # get_meal_display() will return the human readable 
        # description for the meal field
        return f'{self.get_size_display()} size'
    








