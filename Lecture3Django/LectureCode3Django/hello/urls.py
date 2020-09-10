from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("dylan", views.dylan, name="dylan"),
    path("<str:name>", views.greet, name="greet")
]