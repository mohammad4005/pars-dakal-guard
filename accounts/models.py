from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    MANAGER = 'manager'
    GUARD = 'guard'
    ROLE_CHOICES = [(MANAGER, 'مدیر حراست'), (GUARD, 'نگهبان')]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    role = models.CharField(max_length=12, choices=ROLE_CHOICES, default=GUARD)
    phone = models.CharField('شماره همراه', max_length=20, blank=True)
    def __str__(self): return f'{self.user.get_full_name() or self.user.username} - {self.get_role_display()}'
