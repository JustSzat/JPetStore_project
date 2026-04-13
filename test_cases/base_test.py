import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):
    """
    Base Test for each Test Case - opening website
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://petstore.octoperf.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()





