from django.test import TestCase
from restaurant.models import menu  # Assuming standard Django naming (PascalCase)
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token 
from rest_framework.test import APIClient 

class MenuViewTest(TestCase):
    def setUp(self):
        # Create test menu items
        self.item1 = menu.objects.create(
            Title="IceCream",  # Using lowercase field name (common convention)
            Price=80.00,
            Inventory=100
        )
        self.item2 = menu.objects.create(
            Title="Cake",
            Price=500.00,
            Inventory=100
        )
        
        # Create a test user and token
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.token = Token.objects.create(user=self.user)
        
        # Use DRF's APIClient instead of Django's default client
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token.key}')

    def test_get_all_menu_items(self):
        url = reverse('menu')  # Make sure this is your actual URL name
        
        response = self.client.get(url)
        
        # Check if the request was successful
        self.assertEqual(response.status_code, 200)
        
        # Parse JSON response
        response_data = response.json()
        
        expected_data = [
            {'id': self.item1.id,
                'Title': 'IceCream',  # Match your serializer's field names
                'Price': '80.00',      # String if DecimalField returns string
                'Inventory': 100},
            {'id': self.item2.id,
                'Title': 'Cake',
                'Price': '500.00',
                'Inventory': 100}]
        
        self.assertEqual(response_data, expected_data)