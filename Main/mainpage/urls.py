from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('getTen', views.getTen, name="getTenUrl"),
    path('storeAnswer/<int:entryId>/<answer>', views.storeAnswer, name="storeAnswer")
]