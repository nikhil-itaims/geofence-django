from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('gen_ad', views.gen_ad, name='gen_ad'),
]