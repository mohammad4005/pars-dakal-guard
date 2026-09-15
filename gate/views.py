from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import GateLogForm
from .models import GateLog

@login_required
def log_list(request):
    form = GateLogForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        entry = form.save(commit=False)
        entry.recorded_by = request.user
        entry.save()
        messages.success(request, 'تردد با موفقیت ثبت شد.')
        return redirect('gate:list')
    return render(request, 'gate/list.html', {'form': form, 'logs': GateLog.objects.select_related('recorded_by')[:30]})
