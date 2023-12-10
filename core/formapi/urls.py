from django.urls import path
from . import views

urlpatterns = [
    path('', views.formapi, name="formapi"),
]
