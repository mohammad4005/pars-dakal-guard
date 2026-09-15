import uuid
from django.contrib.auth.models import User
from django.db import models
class Checkpoint(models.Model):
    name = models.CharField('نام ایستگاه', max_length=120)
    location_note = models.CharField('محل', max_length=200, blank=True)
    qr_token = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    active = models.BooleanField('فعال', default=True)
    def __str__(self): return self.name
class PatrolMission(models.Model):
    PENDING, DONE, MISSED = 'pending', 'done', 'missed'
    STATES = [(PENDING, 'در انتظار'), (DONE, 'انجام شده'), (MISSED, 'انجام نشده')]
    title = models.CharField('عنوان مأموریت', max_length=150)
    guard = models.ForeignKey(User, on_delete=models.PROTECT, related_name='missions', verbose_name='نگهبان')
    checkpoints = models.ManyToManyField(Checkpoint, verbose_name='ایستگاه‌ها')
    starts_at = models.DateTimeField('شروع')
    ends_at = models.DateTimeField('پایان')
    status = models.CharField('وضعیت', max_length=10, choices=STATES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta: ordering = ['-starts_at']
    def __str__(self): return self.title
class PatrolScan(models.Model):
    mission = models.ForeignKey(PatrolMission, on_delete=models.CASCADE, related_name='scans')
    checkpoint = models.ForeignKey(Checkpoint, on_delete=models.PROTECT)
    scanned_by = models.ForeignKey(User, on_delete=models.PROTECT)
    scanned_at = models.DateTimeField('زمان سرور', auto_now_add=True)
    photo = models.ImageField('عکس زنده', upload_to='patrol/', blank=True)
    note = models.CharField('یادداشت', max_length=300, blank=True)
    class Meta: unique_together = [('mission', 'checkpoint')]
