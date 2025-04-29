from django.db import models

# Create your models here.
class booking(models.Model):
    ID_booking = models.IntegerField()
    Name = models.CharField(max_length=255)
    No_of_guests =models.IntegerField()
    BookingDate = models.DateTimeField()

class menu(models.Model):
    ID_menu = models.IntegerField()
    Tittle = models.CharField(max_length=255)
    Price = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.IntegerField()
