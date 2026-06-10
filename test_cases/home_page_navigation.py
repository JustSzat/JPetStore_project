import unittest
from enum import verify

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import home_page
from pages.catalog_page import CatalogPage
from pages.home_page import HomePage, Locators
from test_cases.base_test import BaseTest
from pages.base_page import BasePage


class HomePageNavigationTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.catalog_page = CatalogPage(self.driver)
        self.home_page.click_enter_the_store()


    def test_navigation_to_home_page(self):
        self.home_page.click_quicklink()
        self.assertTrue(self.home_page.main_picture_is_visible())

    def test_return_to_main_menu(self):
        self.home_page.click_quicklink()
        self.catalog_page.return_to_main_menu()
        website_title = self.driver.title
        print(website_title)
        self.assertIn("JPetStore Demo", website_title)
        self.home_page.search_item("Dogs")
        self.catalog_page.return_to_main_menu()














