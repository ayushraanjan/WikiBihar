from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.retrieve_page, name="retrieve_page"),
    path("search", views.search, name="search"),
    path("new", views.new, name="new_entry"),
    
    

]
