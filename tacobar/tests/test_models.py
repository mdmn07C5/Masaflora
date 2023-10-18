from django.test import TestCase

from tacobar.models import Category, MenuItem


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name="Category Test", slug="category-test")

    def test_category_model_entry(self):
        """Test Category model data insertion/types/field/attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_entry(self):
        """Test Category model return name"""
        data = self.data1
        self.assertEqual(str(data), "Category Test")

class TestMenuItemModel(TestCase):

    def setUp(self):
        Category.objects.create(name="test", slug="test")
        self.data1 = MenuItem.objects.create(category_id=1, name="test1", price=69.42, image="Nonelmao")

    def test_menuitem_model_entry(self):
        """Test Menuitem model return name"""
        data = self.data1
        self.assertEqual(str(data), "test1")