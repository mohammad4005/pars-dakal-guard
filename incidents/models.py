from django.contrib.auth.models import User
from django.db import models
class Incident(models.Model):
    LOW, NORMAL, HIGH = 'low', 'normal', 'high'
    LEVELS = [(LOW, 'کم'), (NORMAL, 'عادی'), (HIGH, 'فوری')]
    title = models.CharField('عنوان واقعه', max_length=160)
    description = models.TextField('شرح')
    severity = models.CharField('اهمیت', max_length=10, choices=LEVELS, default=NORMAL)
    photo = models.ImageField('عکس', upload_to='incidents/', blank=True)
    occurred_at = models.DateTimeField('زمان ثبت', auto_now_add=True)
    reported_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='ثبت‌کننده')
    class Meta: ordering = ['-occurred_at']
    def __str__(self): return self.title
