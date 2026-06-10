import time
import unittest


from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages import catalog_page
from pages import home_page
from pages.catalog_page import CatalogPage, Locators
from pages.home_page import HomePage, Locators
from test_cases.base_test import BaseTest
from pages import catalog_page

from test_data import store_items
import test_data

import sys

from test_data.store_items import load_data


#@ddt
class SearchEngineTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.home_page.click_enter_the_store()
        self.catalog_page = CatalogPage(self.driver)
#        self.data = test_data.store_items.load_data("test_data/data_search.csv")



   # @data(*test_data.store_items.load_data("test_data/data_search.csv"))
   # @unpack

    def test_search_existing_item(self):
        """
        Test of searching existing items
        """
        expected_product = self.catalog_page.enter_and_search_item("Fish")
        results = self.catalog_page.get_fish_results()
        self.assertTrue(any(expected_product.lower() in result.lower() for result in results), f"Product '{expected_product}' not found in search results. "
        f"Actual results: {results}")

    def test_search_no_keyword_visible_error(self):
        """
        Test of searching no keyword and check visibility of error
        """
        self.catalog_page.enter_and_search_item("")
        visible_errors = self.home_page.get_visible_errors()
        print(f"Number of errors: {len(visible_errors)}")
        self.assertTrue(len(visible_errors) > 0)


    def test_no_results(self):
        """
        Test no results by entering invalid keyword
        """
        self.catalog_page.enter_and_search_item("#@#Dd33")
        results = self.driver.find_elements(By.XPATH, '//div[@id="Content"]//tr//a')
        self.assertEqual(len(results), 0)

    def test_results_by_searching_and_by_quicklink(self):
        """
        Test comparing length of list by searching and by quicklink
        """
        self.catalog_page.enter_and_search_item("Fish")
        list_by_entered = self.home_page.get_list_of_searching_products()
        print(f"Number of items are found: {len(list_by_entered)}")
        assert len(list_by_entered) == 2
        self.home_page.click_quicklink()
        list_by_quicklink = self.home_page.get_list_of_linked_product()
        print(f"Number of items are listed by quicklink: {len(list_by_quicklink)}")
        assert len(list_by_quicklink) == 4
        self.assertNotEqual(len(list_by_entered), len(list_by_quicklink))


if __name__ == "__main__":
    unittest.main(verbosity=2)