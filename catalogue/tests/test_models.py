from django.test import TestCase

from catalogue.models import Category, MenuItem, Store

class TestStoresModel(TestCase):
    
    def setUp(self):
        self.data1 = Store.objects.create(
            name='Test Store 1', slug='test-store-1', location='test store 1 location', contact='(332)123-4567'
        )
    


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(
            name="Category Test", slug="category-test")

    def test_category_model_entry(self):
        """Test Category model data insertion/types/field/attributes
        """
        self.assertIsInstance(self.data1, Category)

    def test_category_model_name(self):
        """Test Category model return name"""
        data = self.data1
        self.assertEqual(str(data), "Category Test")


class TestMenuItemModel(TestCase):

    def setUp(self):
        Category.objects.create(name="test", slug="test")
        self.data1 = MenuItem.objects.create(
            category_id=1, name="test1", price=69.42, image="Nonelmao")

    def test_menuitem_model_entry(self):
        """Test Menuitem model return name"""
        data = self.data1
        self.assertEqual(str(data), "test1")
