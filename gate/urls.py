from django.urls import path
from . import views
app_name = 'gate'
urlpatterns = [path('', views.log_list, name='list')]
