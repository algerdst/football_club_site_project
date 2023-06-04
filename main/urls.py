from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("trains", views.trains, name='trains'),
    path("contacts", views.contacts, name='contacts'),

]
