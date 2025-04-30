from rest_framework import serializers
from .models import menu,booking

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = '__all__'


