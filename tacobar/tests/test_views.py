from unittest import skip
from importlib import import_module
from django.conf import settings

from django.test import TestCase, Client, RequestFactory
from django.urls import reverse
from django.http import HttpRequest
from tacobar.models import Category, MenuItem
from tacobar.views import menu_all

# @skip("dummy test to identify which tests are done first")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass


class TestViewResponses(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.c = Client()
        Category.objects.create(name='test-category', slug='test-category')
        self.data1 = MenuItem.objects.create(
            category_id=1, name='test1', slug='test-dish', price=420.69, image="Nonelmao")

    def test_url_allowed_hosts(self):
        """Test allowed hosts
        """
        response = self.c.get('/', HTTP_HOST='noaddress.com')
        self.assertEqual(response.status_code, 400)
        response = self.c.get('/', HTTP_HOST='localhost')
        self.assertEqual(response.status_code, 200)

    def test_menuitem_detail_url(self):
        """Test menuitem reverse and status code
        """
        response = self.c.get(
            reverse(viewname='tacobar:menuitem_detail', args=['test-dish']))
        self.assertEqual(response.status_code, 200)

    def test_category_list_url(self):
        """Test category list reverse and status code"""
        response = self.c.get(
            reverse(viewname='tacobar:category_list', args=['test-category']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_html(self):
        """Test homepage html, without going through browser
        """
        request = HttpRequest()
        session_engine = import_module(settings.SESSION_ENGINE)
        request.session = session_engine.SessionStore()
        response = menu_all(request)
        html = response.content.decode('utf8')
        self.assertIn('RestaurantHomepage', html)
        self.assertTrue(html.startswith('\n<!DOCTYPE html>\n'))
        self.assertEqual(response.status_code, 200)

