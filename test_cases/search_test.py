import time

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
        

