from django.urls import path
from .views import *

urlpatterns = [
    path('api_info', InfoView.as_view(), name='info-api'),

    
]