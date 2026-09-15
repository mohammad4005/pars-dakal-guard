from django.urls import path
from . import views
app_name = 'patrol'
urlpatterns = [path('', views.missions, name='missions'), path('scanner/', views.scanner, name='scanner'), path('scan/<uuid:token>/', views.scan, name='scan'), path('checkpoints/', views.checkpoints, name='checkpoints'), path('checkpoints/<uuid:token>/qr.png', views.checkpoint_qr, name='checkpoint_qr')]
