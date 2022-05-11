from django.contrib import admin
from .models import Squad, Squishmallow, Style

# Register your models here.
admin.site.register(Squishmallow)
admin.site.register(Style)
admin.site.register(Squad)