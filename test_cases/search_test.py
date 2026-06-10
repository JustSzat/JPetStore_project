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
        self.assertIn(expected_product, results,f"Product '{expected_product}' not found in search results. "
        f"Actual results: {results}")

    def test_search_no_keyword(self):
        """
        Test of searching no keyword - visible error
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.Locators.SEARCH_BOX))
        self.home_page.search_btn()
        visible_errors = self.home_page.get_visible_errors()
        self.assertTrue(len(visible_errors) > 0)



    def test_search_no_keyword_number_error(self):
        """
        Test number of errors - negative test
        """
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.Locators.SEARCH_BOX))
        self.home_page.search_btn()
        visible_errors = self.home_page.get_visible_errors()
        expected_errors = ["Please enter a keyword to search for, then press the search button."]
        self.assertCountEqual(visible_errors, expected_errors)


    def test_no_results(self):
        """
        Test no results by entering invalid keyword
        """
        word = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.Locators.SEARCH_BOX))
        word.send_keys("skjdlskd2!")
        self.home_page.search_btn()
        results = self.driver.find_elements(By.XPATH, '//div[@id="Content"]//tr//a')
        self.assertEqual(len(results), 0)

    def test_searching_by_click_and_by_entered(self):
        """
        Test comparing length of list by searching and by click
        """
        self.home_page.search_item("Fish")
        self.home_page.search_btn()
        list_by_entered = self.home_page.get_list_of_searching_products()
        print(len(list_by_entered))
        assert len(list_by_entered) == 2
        self.home_page.click_quicklink()
        list_by_quicklink = self.home_page.get_list_of_linked_product()
        print(len(list_by_quicklink))
        assert len(list_by_quicklink) == 4
        self.assertNotEqual(len(list_by_entered), len(list_by_quicklink))


if __name__ == "__main__":
    unittest.main(verbosity=2)