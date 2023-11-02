from django.test import TestCase

from catalogue.models import Category, MenuItem, Store

class TestStoresModel(TestCase):
    
    def setUp(self):
        self.store = Store.objects.create(name='Test Store 1', slug='test-store-1', location='test store 1 location', contact='(332)123-4567', opening_hours = '8:00', closing_hours='10:00')
        Category.objects.create(name="Category Test 1", slug="category-test-1", store_id=1)
        Category.objects.create(name="Category Test 2", slug="category-test", store_id=1)
        MenuItem.objects.create(category_id=1, name="Menu Item Test 1", price=1.0, image="Nonelmao")
        MenuItem.objects.create(category_id=2, name="Menu Item Test 1", price=1.0, image="Nonelmao")
        MenuItem.objects.create(category_id=2, name="Menu Item Test 1", price=1.0, image="Nonelmao")


    def test_store_db_entry(self):
        db_store = Store.objects.get(id=1)
        self.assertIsInstance(db_store, Store)

    def test_get_categories(self):
        categories = self.store.get_categories()
        self.assertEqual(len(categories), 2)
        for c in categories:
            self.assertEqual(c.store, self.store)

    def test_get_menu(self):
        menu = self.store.get_menu()
        
        for category, items in menu.items():
            self.assertEqual(category.store, self.store)
            for item in items:
                self.assertEqual(item.category, category)
    



class TestCategoriesModel(TestCase):

    def setUp(self):
        Store.objects.create(name='Test Store 1', slug='test-store-1', location='test store 1 location', contact='(332)123-4567', opening_hours = '8:00', closing_hours='10:00')
        self.data1 = Category.objects.create(
            name="Category Test", slug="category-test", store_id=1)
        MenuItem.objects.create(category_id=1, name="Menu Item Test 1", price=1.0, image="Nonelmao")

    def test_category_model_entry(self):
        """Test Category model data insertion/types/field/attributes
        """
        self.assertIsInstance(self.data1, Category)

    def test_category_model_name(self):
        """Test Category model return name"""
        data = self.data1
        self.assertEqual(str(data), "Category Test")

    def test_getmenuitems(self):
        items = self.data1.get_menuitems()
        for item in items:
            self.assertEqual(item.category, self.data1)

class TestMenuItemModel(TestCase):

    def setUp(self):
        self.store = Store.objects.create(name='Test Store 1', slug='test-store-1', location='test store 1 location', contact='(332)123-4567', opening_hours = '8:00', closing_hours='10:00')
        Category.objects.create(name="test", slug="test", store_id=1)
        self.data1 = MenuItem.objects.create(
            category_id=1, name="test1", price=69.42, image="Nonelmao")

    def test_menuitem_model_entry(self):
        """Test Menuitem model return name"""
        data = self.data1
        self.assertEqual(str(data), "test1")
