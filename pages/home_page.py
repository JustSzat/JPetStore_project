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
    VISIBLE_ERRORS = (By.XPATH, '//div[@id = "Content"]/ul[@class = "messages"]')
    QUICKLINK_FISH = (By.XPATH, '//*[@id="QuickLinks"]/a[1]')
    QUICKLINK_REPTILES = (By.XPATH, '//*[@id="QuickLinks"]/a[3]')
    CART = (By.XPATH, '//div[@id = "MenuContent"]/a[contains(@href, "Cart.action")]')

class HomePage(BasePage):

    def search_item(self, word):

        """
        Enter name of an item
        """
        input_item = self.driver.find_element(*Locators.SEARCH_BOX)
        input_item.clear()
        input_item.send_keys(word)



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

        errors = WebDriverWait(self.driver, 5).until(EC.presence_of_all_elements_located(Locators.VISIBLE_ERRORS))
        visible_errors = []
        for e in errors:
            visible_errors.append(e.text)
        return visible_errors

    def get_list_of_searching_products(self):
        products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id = "Catalog"]/table//td/b')))
        products_list =[]
        for p in products:
            products_list.append(p.text)
        return products_list

    def click_quicklink(self):
        quicklink_fish = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(Locators.QUICKLINK_FISH))
        quicklink_fish.click()


    def get_list_of_linked_product(self):
        linked_products = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//div[@id = "Catalog"]/table//td/a')))
        linked_product_list = []
        for lp in linked_products:
            linked_product_list.append(lp.text)
        return linked_product_list




    def click_enter_the_store(self):
        self.driver.find_element(*Locators.enter_click).click()
        time.sleep(6)



