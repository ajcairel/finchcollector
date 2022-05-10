from django.forms import ModelForm
from .models import Style

class StyleForm(ModelForm):
    class Meta:
        model = Style
        fields = ['size']