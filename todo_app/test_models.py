from django.test import TestCase
from .models import Item

class ItemModelTests(TestCase):
    def test_create_item(self):
        # Test creating an Item instance
        item = Item.objects.create(name='Test Item', done=True)
        self.assertEqual(item.name, 'Test Item')
        self.assertTrue(item.done)

    def test_model_str_representation(self):
        # Test the __str__ method of the Item model
        item = Item.objects.create(name='Test Item', done=True)
        self.assertEqual(str(item), 'Test Item')

    def test_default_done_value(self):
        # Test the default value of the 'done' field
        item = Item.objects.create(name='Test Item')
        self.assertFalse(item.done)

    def test_model_query(self):
        # Test querying the database for items
        item1 = Item.objects.create(name='Item 1', done=True)
        item2 = Item.objects.create(name='Item 2', done=False)

        # Retrieve items from the database
        queried_item1 = Item.objects.get(name='Item 1')
        queried_item2 = Item.objects.get(name='Item 2')

        self.assertEqual(queried_item1.done, item1.done)
        self.assertEqual(queried_item2.done, item2.done)
