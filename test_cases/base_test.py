import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):
    """
    Base Test for each Test Case - opening website
    """
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://petstore.octoperf.com")
        self.driver.maximize_window()
        self.driver.implicitly_wait(8)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)



