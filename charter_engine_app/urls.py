from django.urls import path
from .views import home, booking

urlpatterns = [
    path('', home, name='home'),
    path('booking/', booking, name='booking'),
]
