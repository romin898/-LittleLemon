from django.test import TestCase
from restaurant.models import menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = menu.objects.create(Title="IceCream",Price=80,Inventory=100)
        self.assertEqual(str(item),"IceCream : 80")