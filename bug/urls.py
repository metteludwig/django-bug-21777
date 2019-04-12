from django.urls import path

from .views import buggyview

urlpatterns = [
    path('', buggyview),
]
