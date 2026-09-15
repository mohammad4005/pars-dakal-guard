from django import forms
from .models import ShiftHandover
class HandoverForm(forms.ModelForm):
    class Meta:
        model = ShiftHandover
        fields = ['incoming_guard', 'notes', 'equipment_status']
        widgets = {'notes': forms.Textarea(attrs={'rows': 4})}
