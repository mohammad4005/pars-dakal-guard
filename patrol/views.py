from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.urls import reverse
import io
import qrcode
from .forms import ScanForm
from .models import Checkpoint, PatrolMission, PatrolScan

@login_required
def missions(request):
    qs = PatrolMission.objects.filter(guard=request.user).prefetch_related('checkpoints', 'scans')
    return render(request, 'patrol/missions.html', {'missions': qs})

@login_required
def scanner(request):
    return render(request, 'patrol/scanner.html')

@login_required
def scan(request, token):
    checkpoint = get_object_or_404(Checkpoint, qr_token=token, active=True)
    now = timezone.now()
    mission = PatrolMission.objects.filter(guard=request.user, checkpoints=checkpoint, starts_at__lte=now, ends_at__gte=now).order_by('ends_at').first()
    if not mission:
        messages.error(request, 'برای این ایستگاه، مأموریت فعال و معتبر ندارید.')
        return redirect('patrol:missions')
    if PatrolScan.objects.filter(mission=mission, checkpoint=checkpoint).exists():
        messages.info(request, 'این ایستگاه قبلاً ثبت شده است.')
        return redirect('patrol:missions')
    form = ScanForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        item = form.save(commit=False); item.mission = mission; item.checkpoint = checkpoint; item.scanned_by = request.user; item.save()
        if item.mission.scans.count() == item.mission.checkpoints.count():
            item.mission.status = PatrolMission.DONE; item.mission.save(update_fields=['status'])
        messages.success(request, 'بازدید ایستگاه با زمان سرور ثبت شد.')
        return redirect('patrol:missions')
    return render(request, 'patrol/scan.html', {'form': form, 'checkpoint': checkpoint, 'mission': mission})

@login_required
def checkpoints(request):
    return render(request, 'patrol/checkpoints.html', {'checkpoints': Checkpoint.objects.filter(active=True)})

@login_required
def checkpoint_qr(request, token):
    checkpoint = get_object_or_404(Checkpoint, qr_token=token, active=True)
    target = request.build_absolute_uri(reverse('patrol:scan', args=[checkpoint.qr_token]))
    image = qrcode.make(target, border=3, box_size=10)
    data = io.BytesIO()
    image.save(data, format='PNG')
    response = HttpResponse(data.getvalue(), content_type='image/png')
    response['Content-Disposition'] = f'inline; filename="qr-{checkpoint.name}.png"'
    return response
