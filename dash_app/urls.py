from django.urls import path

from dash_app.views import index

urlpatterns = [
    path('', index),
]