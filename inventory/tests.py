from django.test import Client, TestCase
from django.urls import reverse
from rest_framework.status import HTTP_200_OK

from .models import Inventory, Supplier


class InventoryApiTest(TestCase):
    url = '/api/inventory/'

    def setUp(self):
        self.client = Client()

    def test_inventory_list_api(self):
        """Inventory List API should return 200 """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTP_200_OK)


class InventoryWebTest(TestCase):

    def setUp(self):
        self.client = Client()    

    def test_inventory_list_web_page(self):
        """Inventory List should return 200 """
        response = self.client.get(reverse('inventory'))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_inventory_detail_web_page(self):
        """Inventory Detail should return 200 """
        supplier = Supplier.objects.create(name='john smith')
        inventory = Inventory.objects.create(
            name='Lunch Box',
            description='SS Lunch Box',
            note='test note',
            stock=300,
            availability=True,
            supplier=supplier
        )
        response = self.client.get(reverse('inventory_detail', args=[inventory.id]))
        self.assertEqual(response.status_code, HTTP_200_OK)
