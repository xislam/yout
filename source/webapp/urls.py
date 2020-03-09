from django.urls import path
from . import views

urlpatterns = [
    path('', views.download, name='get_link'),


]