from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
# import json
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User


class MenuViewTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='test_user')
        user.set_password('test_password')
        user.save()
        Token.objects.create(user=user)
        
        # Include an appropriate `Authorization:` header on all requests.
        token = Token.objects.get(user__username='test_user')
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        
        # self.client = APIClient()
        self.menu1 = Menu.objects.create(title="Burger", price=10, inventory=50)
        self.menu2 = Menu.objects.create(title="Pizza", price=15, inventory=30)
        self.menu3 = Menu.objects.create(title="Pasta", price=12, inventory=40)

    def test_menu_db(self):
        items = Menu.objects.all()
        self.assertEqual(len(items), 3)
    
    def test_getall(self):
        response = self.client.get('/restaurant/menu-items')
        # print(response)
        # json_response = json.loads(response.content)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, 200)