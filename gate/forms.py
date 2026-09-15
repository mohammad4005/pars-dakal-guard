from django import forms
from .models import GateLog
class GateLogForm(forms.ModelForm):
    class Meta:
        model = GateLog
        fields = ['kind', 'direction', 'full_name', 'national_id', 'vehicle_plate', 'company', 'note']
        widgets = {'note': forms.Textarea(attrs={'rows': 3})}
