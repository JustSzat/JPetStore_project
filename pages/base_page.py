from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()


    def find_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def visible_element_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    def visible_all_elements_located(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    def element_clickable(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.element_clickable(locator).click()

    def send_keys(self, locator, text):
        element = self.find_element_located(locator)
        element.clear()
        element.send_keys(text)

    def _verify_page(self):
        return