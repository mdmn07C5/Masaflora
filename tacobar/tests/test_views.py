from unittest import skip

from django.test import TestCase, Client
from django.urls import reverse
from tacobar.models import Category, MenuItem
from tacobar import views

# @skip("dummy test to identify which tests are done first")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
        Category.objects.create(name='test', slug='test')
        self.data1 = MenuItem.objects.create(category_id=1, name='test1', slug='test-dish', price=420.69, image="Nonelmao")
    
    def test_url_allowed_hosts(self):
        """Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_menuitem_detail_url(self):
        response = self.c.get(reverse(viewname='tacobar:menuitem_detail',args=['test-dish']))
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """Test homepage response status
        """
        pass
