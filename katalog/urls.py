from django.urls import path
from katalog.views import show_katalog

app_name = 'tugas2'

urlpatterns = [
    path('', show_katalog, name='show_katalog'),
]