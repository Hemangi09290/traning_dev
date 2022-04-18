from django.urls import path
from hello import views

#This url will route to home page through views
urlpatterns = [
    path("", views.home, name="home"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("hello/<name>", views.getData, name="getData"),
]