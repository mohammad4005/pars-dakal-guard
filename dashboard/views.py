from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from patrol.models import PatrolMission
from incidents.models import Incident
from gate.models import GateLog
from accounts.views import manager_required
@login_required
def home(request):
    today = timezone.localdate()
    missions = PatrolMission.objects.select_related('guard').filter(starts_at__date=today)
    return render(request, 'dashboard/home.html', {'missions': missions[:10], 'done': missions.filter(status='done').count(), 'pending': missions.filter(status='pending').count(), 'missed': missions.filter(status='missed').count(), 'incidents': Incident.objects.filter(occurred_at__date=today)[:8], 'gate_logs': GateLog.objects.filter(recorded_at__date=today)[:8]})

@manager_required
def reports(request):
    today = timezone.localdate()
    return render(request, 'dashboard/reports.html', {'date': today, 'gate_count': GateLog.objects.filter(recorded_at__date=today).count(), 'incident_count': Incident.objects.filter(occurred_at__date=today).count(), 'missions': PatrolMission.objects.select_related('guard').filter(starts_at__date=today)})
