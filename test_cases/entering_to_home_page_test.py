import unittest



from selenium.webdriver.support.wait import WebDriverWait

from pages.home_page import HomePage
from test_cases.base_test import BaseTest


class EnterToHomePageTest(BaseTest):
    def test_entering_to_home(self):
        home_page = HomePage(self.driver)
        home_page.click_enter_the_store()




