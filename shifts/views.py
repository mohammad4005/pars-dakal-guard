from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils import timezone
from .forms import HandoverForm
from .models import ShiftHandover
@login_required
def list_create(request):
    form = HandoverForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False); item.outgoing_guard = request.user; item.save()
        messages.success(request, 'تحویل شیفت ثبت شد.'); return redirect('shifts:list')
    return render(request, 'shifts/list.html', {'form': form, 'items': ShiftHandover.objects.select_related('outgoing_guard', 'incoming_guard')[:30]})
@login_required
def acknowledge(request, pk):
    item = ShiftHandover.objects.get(pk=pk)
    if request.user == item.incoming_guard and not item.acknowledged_at:
        item.acknowledged_at = timezone.now(); item.save(); messages.success(request, 'تحویل شیفت تأیید شد.')
    return redirect('shifts:list')
