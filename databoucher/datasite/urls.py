from django.urls import path

from . import views

app_name = 'datasite'

urlpatterns = [
    path('', views.index, name='index'),
]