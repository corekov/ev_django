from django import forms
from .models import County

class CountyForm(forms.ModelForm):
    class Meta:
        model = County
        fields = ['name', 'state']
        labels = {
            'name': 'Название округа',
            'state': 'Штат',
        }
