from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter



urlpatterns = [
    path('airesponse/', views.seeeeeeeed, name='reci'),
    path('airesp/',views.seeeeeeed,name='inp')
]