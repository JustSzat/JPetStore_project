from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import home_page
from pages.base_page import BasePage
from pages.home_page import HomePage, Locators




class Locators:
    RETURN_TO_MAIN_MENU = (By.XPATH, '//div[@id = "BackLink"]/a')
    IGUANA_BTN = (By.XPATH, '//div[@id="Catalog"]//tr//a[contains(@href, "RP-LI-02")]')
    IGUANA = (By.XPATH, '//div[@id = "Catalog"]//td[contains(., "RP-LI-02")]')
    IGUANA_TO_CART = (By.XPATH, '//div[@id = "Catalog"]//td/a[contains(@href, "EST-13") and contains(text(), "Add to Cart")]')
    GOLDFISH_BTN = (By.XPATH, '//div[@id="Catalog"]//td//a[contains(@href, "FI-FW-02")]')
    GOLDFISH_FEMALE = (By.XPATH, '//div[@id="Catalog"]//tr//td//a[contains(@href, "EST-21") and @class = "Button"]')
    GOLDFISH_FEMALE_TO_CART = (By.XPATH, '//div[@id = "Catalog"]//td/a[contains(@href, "EST-21") and contains(text(), "Add to Cart")]')
    POODLE = (By.XPATH, '//div[@id = "Catalog"]//tr/td/a[contains(@href, "K9-PO-02")]')
    FISH_RESULTS = (By.XPATH, '//div[@id = "Catalog"]//b')



class CatalogPage(BasePage):

    def enter_and_search_item(self, word):

        """
        Enter name of an item and click 'Search'
        """
        self.type(Locators.home_page.SEARCH_BOX, word)
        self.click(Locators.home_page.SEARCH_BTN)

    def get_fish_results(self):
        self.find_all(Locators.FISH_RESULTS)


    def select_iguana(self):
        self.click(Locators.IGUANA_BTN)

    def select_goldfish(self):
        self.click(Locators.GOLDFISH_BTN)

    def select_goldfish_female(self):
        self.click(Locators.GOLDFISH_FEMALE)

    def get_item_locator(self, item_name):
        return ()

    def get_iguana(self):
        return self.find(Locators.IGUANA).text
    def return_to_main_menu(self):
        self.click(Locators.RETURN_TO_MAIN_MENU)