from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vintage/', views.vintage, name='vintage'),
    path('minimalismo/', views.minimalismo, name='minimalismo'),
    path('sostenible/', views.sostenible, name='sostenible'),
    path('accesorios/', views.accesorios, name='accesorios'),
    path('suscribirse/', views.suscribirse, name='suscribirse'),
]


