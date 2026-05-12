
from pydoc import text

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class Locators:
    ENTER_CLICK = (By.LINK_TEXT, 'Enter the Store')
    MAIN_PICTURE = (By.ID, 'MainImageContent')
    SIGN_IN = (By.XPATH, '//*[@id="MenuContent"]/a[2]')
    CART = (By.XPATH, '//*[@id="MenuContent"]/a[1]')
    FAQ = (By.XPATH, '//*[@id="MenuContent"]/a[3]')
    SEARCH_BOX = (By. XPATH, '//*[@id="SearchContent"]/form/input[@name="keyword"]')
    SEARCH_BTN = (By.XPATH, '//*[@id="SearchContent"]/form/input[@name = "searchProducts"]')
    LIST_OF_PRODUCTS = (By.XPATH, '//div[@id = "Catalog"]/table//td/b')
    LINKED_LINKS = (By.XPATH, '//div[@id = "Catalog"]/table//td/a')
    VISIBLE_ERRORS = (By.XPATH, '//div[@id = "Content"]/ul[@class = "messages"]')
    QUICKLINK_FISH = (By.XPATH, '//*[@id="QuickLinks"]/a[1]')
    FOUND_FISH  = (By.XPATH, '//div[@id="Catalog"]//tr[position() > 1] ')
    QUICKLINK_REPTILES = (By.XPATH, '//*[@id="QuickLinks"]/a[3]')
    FOUND_REPTILES = (By.XPATH, '//div[@id="Catalog"]//tr[position() > 1] ')
    CART = (By.XPATH, '//div[@id = "MenuContent"]/a[contains(@href, "Cart.action")]')

class HomePage(BasePage):


    def search_item(self, word):

        """
        Enter name of an item
        """
        self.type(Locators.SEARCH_BOX, word)
        self.click(Locators.SEARCH_BTN)

    def get_visible_errors(self):

        errors = self.find_all(Locators.VISIBLE_ERRORS)
        visible_errors = []
        for e in errors:
            visible_errors.append(e.text)
        return visible_errors

    def get_list_of_searching_products(self):
        products = self.find_all(Locators.LIST_OF_PRODUCTS)
        products_list =[]
        for p in products:
            products_list.append(p.text)
        return products_list

    def click_quicklink(self):
        self.click(Locators.QUICKLINK_FISH)

    def get_list_of_linked_product(self):
        linked_products = self.find_all(Locators.LINKED_LINKS)
        linked_product_list = []
        for lp in linked_products:
            linked_product_list.append(lp.text)
        return linked_product_list

    def click_enter_the_store(self):
        self.click(Locators.ENTER_CLICK)




