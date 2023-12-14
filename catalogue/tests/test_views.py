from unittest import skip
from importlib import import_module
from django.conf import settings

from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.http import HttpRequest
from catalogue.models import Category, MenuItem, Store
from catalogue.views import menu_all, store_page, store_all

# @skip("dummy test to identify which tests are done first")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.c = Client()
        self.store = Store.objects.create(
            name="Test Store 1",
            slug="test-store-1",
            location="test store 1 location",
            contact="(332)123-4567",
            opening_hours="8:00",
            closing_hours="10:00",
        )
        self.category = Category.objects.create(
            name="test-category", slug="test-category", store_id=1
        )
        self.data1 = MenuItem.objects.create(
            category_id=1,
            store_id=1,
            name="test1",
            slug="test-dish",
            price=420.69,
            image="Nonelmao",
        )

    def test_url_allowed_hosts(self):
        """Test allowed hosts"""
        response = self.c.get("/", HTTP_HOST="noaddress.com")
        self.assertEqual(response.status_code, 400)
        response = self.c.get("/", HTTP_HOST="localhost")
        # we're redirecting homepage (for now)
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.status_code, 302)

    def test_menuitem_detail_url(self):
        """Test menuitem reverse and status code"""
        response = self.c.get(
            reverse(
                viewname="catalogue:detail",
                args=["test-category", "test-dish"],
            )
        )
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        """Test category list reverse and status code"""
        response = self.c.get(
            reverse(viewname="catalogue:category_list", args=["test-category"])
        )
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """Test homepage html, without going through browser"""
        request = HttpRequest()
        session_engine = import_module(settings.SESSION_ENGINE)
        request.session = session_engine.SessionStore()
        response = menu_all(request)
        html = response.content.decode("utf8")
        self.assertIn("RestaurantHomepage", html)
        self.assertTrue(html.startswith("\n<!DOCTYPE html>\n"))
        self.assertEqual(response.status_code, 200)

    def test_store_page(self):
        request = HttpRequest()
        session_engine = import_module(settings.SESSION_ENGINE)
        request.session = session_engine.SessionStore()
        response = store_page(request, self.store.slug)

        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf8")
        # self.assertIn(self.store.slug, html) # we don't actually put the name or slug in the page yet
        self.assertIn(self.category.slug, html)
        self.assertIn(self.data1.slug, html)

    def test_store_all(self):
        request = HttpRequest()
        session_engine = import_module(settings.SESSION_ENGINE)
        request.session = session_engine.SessionStore()
        response = store_all(request)

        self.assertEqual(response.status_code, 200)
        html = response.content.decode("utf8")
        self.assertIn(self.store.name, html)
