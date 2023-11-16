from django.test import TestCase
from django.urls import reverse
from .models import Item
from .forms import ItemForm

class TodoViewsTests(TestCase):
    def setUp(self):
        self.item = Item.objects.create(name='Test Item', done=False)
        self.edit_item_url = reverse('edit', args=[self.item.id])
        self.toggle_item_url = reverse('toggle', args=[self.item.id])
        self.delete_item_url = reverse('delete', args=[self.item.id])

    def test_get_todo_list_view(self):
        response = self.client.get(reverse('get_todo_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo_list.html')

    def test_add_item_view(self):
        response = self.client.post(reverse('add_item'), {'name': 'New Item'})
        self.assertEqual(response.status_code, 302)  # Redirect status
        self.assertRedirects(response, reverse('get_todo_list'))

    def test_edit_item_view(self):
        response = self.client.get(self.edit_item_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_item.html')

        response = self.client.post(self.edit_item_url, {'name': 'Updated Item'})
        self.assertEqual(response.status_code, 302)  # Redirect status
        self.assertRedirects(response, reverse('get_todo_list'))
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, 'Updated Item')

    def test_toggle_item_view(self):
        response = self.client.post(self.toggle_item_url)
        self.assertEqual(response.status_code, 302)  # Redirect status
        self.assertRedirects(response, reverse('get_todo_list'))
        self.item.refresh_from_db()
        self.assertTrue(self.item.done)

    def test_delete_item_view(self):
        response = self.client.post(self.delete_item_url)
        self.assertEqual(response.status_code, 302)  # Redirect status
        self.assertRedirects(response, reverse('get_todo_list'))
        self.assertFalse(Item.objects.filter(id=self.item.id).exists())
