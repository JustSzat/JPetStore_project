import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import home_page
from pages.home_page import HomePage
from test_cases.base_test import BaseTest
from test_data import store_items


class SearchEngineTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.home_page.click_enter_the_store()

    def test_search_existing_item(self):
        self.home_page.search_item("Fish")
        self.home_page.search_btn()
        results = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id ="Catalog"]//*[contains(text(), "fish") or contains(text(), "Fish")]')))
        self.assertTrue(len(results) > 0)
        time.sleep(5)

    def test_search_no_item(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.Locators.SEARCH_BOX))
        self.home_page.search_btn()
        visible_errors = self.home_page.get_visible_errors()
        self.assertTrue(len(visible_errors) > 0)
        time.sleep(5)

    def test_search_no_item_error(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(home_page.Locators.SEARCH_BOX))
        self.home_page.search_btn()
        visible_errors = self.home_page.get_visible_errors()
        expected_errors = ["Please enter a keyword to search for, then press the search button."]
        self.assertCountEqual(visible_errors, expected_errors)
        time_sleep(5)


if __name__ == "__main__":
    unittest.main(verbosity=2)