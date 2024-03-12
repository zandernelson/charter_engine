from django.shortcuts import render

def home(request):
    return render(request, 'charter_engine_app/home.html')

def booking(request):
    return render(request, 'charter_engine_app/booking.html')