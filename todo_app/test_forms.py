from django.test import TestCase
from .forms import ItemForm
from .models import Item

class ItemFormTests(TestCase):
    def test_valid_form(self):
        data = {'name': 'Test Item', 'done': True}
        form = ItemForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        data = {'name': '', 'done': True}
        form = ItemForm(data=data)
        self.assertFalse(form.is_valid())



class ItemFormSavingTests(TestCase):
    def test_form_save(self):
        data = {'name': 'Test Item', 'done': True}
        form = ItemForm(data=data)
        self.assertTrue(form.is_valid())
        item = form.save()
        self.assertEqual(item.name, 'Test Item')
        self.assertTrue(item.done)


class ItemFormFieldTests(TestCase):
    def test_name_field_max_length(self):
        max_length = ItemForm.base_fields['name'].max_length
        self.assertEqual(max_length, 50)