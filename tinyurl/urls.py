from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shortenurl/',views.shortenurl,name='shortenurl'),
    path('<sURL>/',views.longURL,name='longURL'),
]
