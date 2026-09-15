from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import IncidentForm
from .models import Incident

@login_required
def list_create(request):
    form = IncidentForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False)
        item.reported_by = request.user
        item.save()
        messages.success(request, 'واقعه ثبت شد.')
        return redirect('incidents:list')
    return render(request, 'incidents/list.html', {'form': form, 'items': Incident.objects.select_related('reported_by')[:30]})
