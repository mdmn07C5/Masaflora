from unittest import skip

from django.test import TestCase, Client

from tacobar.models import Category, MenuItem
from tacobar import views

# @skip("dummy test to identify which tests are done first")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass

class TestViewResponses(TestCase):
    def setUp(self):
        self.c = Client()
    
    def test_url_allowed_hosts(self):
        """Test allowed hosts
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_url(self):
        """Test homepage response status
        """
        pass
