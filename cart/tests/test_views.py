from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from catalogue.models import Category, MenuItem, Store
from account.models import UserBase


class TestCartView(TestCase):
    def setUp(self):
        UserBase.objects.create(user_name="admin")
        Store.objects.create(
            name="Test Store 1",
            slug="test-store-1",
            location="test store 1 location",
            contact="(332)123-4567",
            opening_hours="8:00",
            closing_hours="10:00",
        )
        Category.objects.create(name="test_category", slug="test-category", store_id=1)
        MenuItem.objects.create(
            category_id=1,
            store_id=1,
            name="test dish",
            slug="test-dish",
            price=1.00,
            image="Nonelmao",
        )
        MenuItem.objects.create(
            category_id=1,
            store_id=1,
            name="test dish 2",
            slug="test-dish-2",
            price=2.00,
            image="Nonelmao",
        )
        MenuItem.objects.create(
            category_id=1,
            store_id=1,
            name="test dish 3",
            slug="test-dish-3",
            price=3.00,
            image="Nonelmao",
        )

        self.client.post(
            reverse("cart:cart_add"),
            {"menuitemid": 2, "menuitemqty": 1, "action": "post"},
            xhr=True,
        )
        self.client.post(
            reverse("cart:cart_add"),
            {"menuitemid": 1, "menuitemqty": 1, "action": "post"},
            xhr=True,
        )
        response = self.client.post(
            reverse("cart:cart_add"),
            {"menuitemid": 3, "menuitemqty": 1, "options": {}, "action": "post"},
            xhr=True,
        )

    def test_cart_url(self):
        """Test cart homepage"""
        response = self.client.get(reverse("cart:cart_summary"))
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        """test adding to cart"""
        response = self.client.post(
            reverse("cart:cart_add"),
            {"menuitemid": 3, "menuitemqty": 1, "options": {}, "action": "post"},
            xhr=True,
        )
        self.assertEqual(
            response.json(),
            {"qty": 4, "sub_total": "3.00", "total": "9.00"},
        )

    def test_cart_delete(self):
        """test removing from cart"""
        response = self.client.post(
            reverse("cart:cart_delete"), {"item_index": 0, "action": "post"}, xhr=True
        )
        self.assertEqual(response.json(), {"qty": 2, "total": "4.00"})
