from django.test import TestCase
from django.test.client import Client
from mainapp.models import Product, ProductCategory
from django.core.management import call_command


class TestMainappSmoke(TestCase):
    status_code_success = 200

    def setUp(self):
        cat_1 = ProductCategory.objects.create(name='cat_1')
        for i in range(50):
            Product.objects.create(category=cat_1, name=f'prod_{i}')
        self.client = Client()

    def get_products_item(self):
        return Product.objects.all()

    def get_category_item(self):
        return ProductCategory.objects.all()

    def test_mainapp_urls(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, self.status_code_success)

        response = self.client.get('/contact/')
        self.assertEqual(response.status_code, self.status_code_success)

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, self.status_code_success)

        response = self.client.get('/products/category/0/')
        self.assertEqual(response.status_code, self.status_code_success)

    def test_products_urls(self):
        for category_item in self.get_category_item():
            response = self.client.get(f'/products/category/{category_item.pk}/')
            self.assertEqual(response.status_code, self.status_code_success)

        for product_item in self.get_products_item():
            response = self.client.get(f'/products/product/{product_item.pk}/')
            self.assertEqual(response.status_code, self.status_code_success)

    def tearDown(self):
        call_command('sqlsequencereset', 'mainapp', 'authapp', 'ordersapp', 'basketapp')

