from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from catalogue.models import Category, MenuItem

class TestBasketView(TestCase):

    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name='test_category', slug='test-category')
        MenuItem.objects.create(category_id=1, name='test dish', slug='test-dish', price=1.00, image="Nonelmao")
        MenuItem.objects.create(category_id=1, name='test dish 2', slug='test-dish-2', price=2.00, image="Nonelmao")
        MenuItem.objects.create(category_id=1, name='test dish 3', slug='test-dish-3', price=3.00, image="Nonelmao")

        self.client.post(
            reverse('cart:cart_add'), {'menuitemid':2, 'menuitemqty':10, 'action': 'post'}, xhr=True
        )
        self.client.post(
            reverse('cart:cart_add'), {'menuitemid':1, 'menuitemqty':1, 'action': 'post'}, xhr=True
        )

    def test_cart_url(self):
        """Test cart homepage"""
        response = self.client.get(reverse('cart:cart_summary'))
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        """test adding to cart"""
        response = self.client.post(
            reverse('cart:cart_add'), {'menuitemid':3, 'menuitemqty':1, 'action': 'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 12, 'item_qty':1, 'sub_total':'3.00', 'total':'24.00'})

    def test_cart_delete(self):
        """test removing from cart"""
        response = self.client.post(
            reverse('cart:cart_delete'), {'menuitemid':2, 'action':'post'}, xhr=True
        )
        self.assertEqual(response.json(), {'qty': 1, 'total': '1.00'})