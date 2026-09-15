from django.urls import path
from . import views
app_name = 'shifts'
urlpatterns = [path('', views.list_create, name='list'), path('<int:pk>/acknowledge/', views.acknowledge, name='acknowledge')]
