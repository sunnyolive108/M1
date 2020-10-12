

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contribution/', views.contribution, name='contribution'),
    path('thankyou/', views.thankyou, name='thankyou'),
]
