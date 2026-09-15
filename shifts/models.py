from django.contrib.auth.models import User
from django.db import models
class ShiftHandover(models.Model):
    outgoing_guard = models.ForeignKey(User, on_delete=models.PROTECT, related_name='outgoing_handovers', verbose_name='تحویل‌دهنده')
    incoming_guard = models.ForeignKey(User, on_delete=models.PROTECT, related_name='incoming_handovers', verbose_name='تحویل‌گیرنده')
    notes = models.TextField('وضعیت و موارد قابل پیگیری')
    equipment_status = models.CharField('وضعیت تجهیزات', max_length=200, blank=True)
    created_at = models.DateTimeField('زمان ثبت', auto_now_add=True)
    acknowledged_at = models.DateTimeField('زمان تأیید', null=True, blank=True)
    class Meta: ordering = ['-created_at']
