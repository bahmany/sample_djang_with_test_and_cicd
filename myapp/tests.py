from django.test import TestCase
from .models import Item


class ItemModelTest(TestCase):

    def setUp(self):
        Item.objects.create(name="Test Item", description="Test Description")

    def test_item_creation(self):
        item = Item.objects.get(name="Test Item")
        self.assertEqual(item.description, "Test Description")


class IndexViewTest(TestCase):

    def setUp(self):
        Item.objects.create(name="Test Item 1", description="Test Description 1")
        Item.objects.create(name="Test Item 2", description="Test Description 2")

    def test_index_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Item 1")
        self.assertContains(response, "Test Item 2")
