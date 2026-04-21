import unittest
from enum import verify

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import home_page
from pages.home_page import HomePage, Locators
from test_cases.base_test import BaseTest


class HomePageNavigationTest(BaseTest):

    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)


    def test_navigation_to_home_page(self):
        self.home_page.click_enter_the_store()
        home_pic = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(home_page.Locators.main_picture))
        self.assertTrue(home_pic.is_displayed())











