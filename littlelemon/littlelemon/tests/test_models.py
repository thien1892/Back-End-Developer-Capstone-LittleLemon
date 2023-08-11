from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80.0, inventory=100)
        itemstr = item.__str__()
        self.assertEqual(itemstr, "IceCream : 80.0")
    def test_fields(self):
        item = Menu.objects.create(title="IceCream", price=80.0, inventory=100)
        self.assertIsInstance(item.price, float)
        self.assertIsInstance(item.inventory, int)
        self.assertIsInstance(item.title, str)
