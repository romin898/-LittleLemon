from django.shortcuts import render
from rest_framework import generics 
from .serializers import MenuSerializer,BookingSerializer
from .models import menu,booking
from rest_framework import viewsets

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = BookingSerializer