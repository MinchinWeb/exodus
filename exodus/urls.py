from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('people', views.person.PersonIndex.as_view()),
    path('people/<int:pk>', views.person.PersonDetails.as_view())
]
