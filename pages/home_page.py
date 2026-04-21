import time
from pydoc import text

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class Locators:
    enter_click = (By.LINK_TEXT, 'Enter the Store')
    main_picture = (By.ID, 'MainImageContent')
    SIGN_IN = (By.XPATH, '//*[@id="MenuContent"]/a[2]')
    CART = (By.XPATH, '//*[@id="MenuContent"]/a[1]')
    FAQ = (By.XPATH, '//*[@id="MenuContent"]/a[3]')
    SEARCH_BOX = (By. XPATH, '//*[@id="SearchContent"]/form/input[@name="keyword"]')
    SEARCH_BTN = (By.XPATH, '//*[@id="SearchContent"]/form/input[@name = "searchProducts"]')
    VISIBLE_ERRORS = (By. XPATH, '//div[@id = "Content"]/ul[@class = "messages"]')

class HomePage(BasePage):

    def search_item(self, text):

        """
        Enter some name item
        """
        input_item = self.driver.find_element(*Locators.SEARCH_BOX)
        input_item.clear()
        input_item.send_keys(text)

    def search_btn(self):

        """
        Click btn 'Search'
        """
        self.driver.find_element(*Locators.SEARCH_BTN).click()

    def get_number_of_errors_message(self):
        """
        Get number of errors message
        """
        return self.driver.find_element

    def get_visible_errors(self):

        errors = self.driver.find_elements(*Locators.VISIBLE_ERRORS)
        visible_errors = []
        for e in errors:
            visible_errors.append(e.text)
        return visible_errors



    def click_enter_the_store(self):
        self.driver.find_element(*Locators.enter_click).click()
        time.sleep(6)



