from django.shortcuts import render
from rest_framework import generics
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets
# Create your views here.

def index(request):
    return render(request, 'index_lab.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer