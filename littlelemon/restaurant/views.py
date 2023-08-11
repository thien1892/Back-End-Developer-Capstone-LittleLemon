from django.shortcuts import render
from rest_framework import generics
from .models import Booking, Menu
from .serializers import MenuSerializer, BookingSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
# Create your views here.

def index(request):
    return render(request, 'index_lab.html', {})

class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class SingleMenuItemsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [IsAuthenticated]

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]