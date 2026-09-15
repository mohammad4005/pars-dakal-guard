from django import forms
from .models import Incident
class IncidentForm(forms.ModelForm):
    class Meta:
        model = Incident
        fields = ['title', 'severity', 'description', 'photo']
        widgets = {'description': forms.Textarea(attrs={'rows': 4}), 'photo': forms.FileInput(attrs={'accept': 'image/*', 'capture': 'environment'})}
