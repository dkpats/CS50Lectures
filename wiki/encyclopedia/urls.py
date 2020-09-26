from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.entry, name="entry"),
    path("search/", views.search, name="search"),
    path("random/", views.randomEntry, name="randomEntry"),
    path("newEntry/", views.newEntry, name="newEntry"),
    path("saveNewEntry/", views.saveNewEntry, name="saveNewEntry"),
    path("editEntryPage/", views.editEntryPage, name="editEntryPage"),
    path("saveEntryEdits/", views.saveEntryEdits, name="saveEntryEdits")
]