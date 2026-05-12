from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()


    def find(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)

    def find_all(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def click(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        element.click()

    def type(self, locator, text):
        element = self.find(locator)
        element.clear()
        element.send_keys(text)

    def _verify_page(self):
        return