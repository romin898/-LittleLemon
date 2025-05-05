from django.shortcuts import render
from rest_framework import generics 
from .serializers import MenuSerializer,BookingSerializer
from .models import menu,booking
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    perimission_classes = [IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView,generics.DestroyAPIView):
    perimission_classes = [IsAuthenticated]
    queryset = menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    perimission_classes = [IsAuthenticated]
    queryset = booking.objects.all()
    serializer_class = BookingSerializer