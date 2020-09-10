from selenium import webdriver
from django.test import TestCase


class BasicTests(TestCase):

    def test_opens_django_admin_page(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://127.0.0.1:8000/admin')
        assert 'admin' in self.browser.title

    def tearDown(self):
        self.browser.close()
