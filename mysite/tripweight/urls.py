from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.table, name='table')
]