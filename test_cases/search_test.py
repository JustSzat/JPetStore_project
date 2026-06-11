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

    def test_search_existing_item(self):
        """
        Test of searching existing items
        """
        # enter "Fish" in the search engine
        expected_product = self.catalog_page.enter_and_search_item("Fish")
        # get founded results
        results = self.catalog_page.get_fish_results()
        # verify that results contain at least one product with "Fish"
        self.assertTrue(any(expected_product.lower() in result.lower() for result in results), f"Product '{expected_product}' not found in search results. "
        f"Actual results: {results}")

    def test_search_with_empty_input(self):
        """
        Test of searching with empty input and check visibility of error
        """
        # enter an empty string in the search engine
        self.catalog_page.enter_and_search_item("")
        # get visible error messages
        visible_errors = self.home_page.get_visible_errors()
        print(f"Number of errors: {len(visible_errors)}")
        # verify that at least 1 error message is displayed
        self.assertTrue(len(visible_errors) > 0)


    def test_search_invalid_input_returns_no_results(self):
        """
        Test searching of invalid input returns no results
        """
        # enter invalid input in the search engine
        self.catalog_page.enter_and_search_item("#@#Dd33")
        # get founded results
        results = self.driver.find_elements(By.XPATH, '//div[@id="Content"]//tr//a')
        # verify that no results are returned
        self.assertEqual(len(results), 0)

    def test_results_by_searching_and_by_quicklink(self):
        """
        Test comparing length of list by searching and by quicklink
        """
        # enter "Fish" in the search engine
        self.catalog_page.enter_and_search_item("Fish")
        #get list of founded products
        list_by_entered = self.home_page.get_list_of_searching_products()
        print(f"Number of items are found: {set(list_by_entered)}")
        # open category Fish using the quick link
        self.home_page.click_quicklink()
        # get list of available products
        list_by_quicklink = self.home_page.get_list_of_linked_product()
        print(f"Number of items are listed by quicklink: {set(list_by_quicklink)}")
        # verify that both methods return different numbers of products
        self.assertNotEqual(set(list_by_entered), set(list_by_quicklink))


if __name__ == "__main__":
    unittest.main(verbosity=2)