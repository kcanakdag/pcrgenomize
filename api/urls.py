from django.urls import path
from . import views

urlpatterns = [
    path('PCRendpoint/', views.get_data),
]

