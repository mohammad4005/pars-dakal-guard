from django.contrib.auth.models import User
from django.db import models

class GateLog(models.Model):
    PERSON, VEHICLE = 'person', 'vehicle'
    KIND = [(PERSON, 'فرد'), (VEHICLE, 'خودرو')]
    IN, OUT = 'in', 'out'
    DIRECTION = [(IN, 'ورود'), (OUT, 'خروج')]
    kind = models.CharField('نوع', max_length=10, choices=KIND)
    direction = models.CharField('جهت', max_length=5, choices=DIRECTION)
    full_name = models.CharField('نام شخص / راننده', max_length=120)
    national_id = models.CharField('کد ملی', max_length=20, blank=True)
    vehicle_plate = models.CharField('پلاک خودرو', max_length=30, blank=True)
    company = models.CharField('شرکت / مقصد', max_length=120, blank=True)
    note = models.TextField('توضیحات', blank=True)
    recorded_at = models.DateTimeField('زمان ثبت', auto_now_add=True)
    recorded_by = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='ثبت‌کننده')
    class Meta:
        ordering = ['-recorded_at']
    def __str__(self): return f'{self.get_direction_display()} {self.full_name}'
