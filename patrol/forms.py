from django import forms
from .models import PatrolScan
class ScanForm(forms.ModelForm):
    class Meta:
        model = PatrolScan
        fields = ['photo', 'note']
        widgets = {'photo': forms.FileInput(attrs={'accept': 'image/*', 'capture': 'environment'}), 'note': forms.TextInput()}
