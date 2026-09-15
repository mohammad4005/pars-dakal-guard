from django.contrib import admin
from .models import Checkpoint, PatrolMission, PatrolScan
admin.site.register(Checkpoint)
admin.site.register(PatrolMission)
admin.site.register(PatrolScan)
