from django.urls import path
from . import views

urlpatterns = [
    path('getimage', views.getimage, name='getimage'),
    path('uploaddata', views.uploaddata, name='uploaddata'),
    path('viewimage', views.viewimage, name='viewimage'),

]
