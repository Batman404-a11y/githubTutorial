from django.urls import path
from . import views
app_name="homeApp"
urlpatterns=[
    path("",views.index,name="index"),
    path("hai",views.haindex,name="haindex"),
    path("fillit",views.fillit,name="fillit")
]