from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class Locators:
    RETURN_TO_MAIN_MENU = (By. XPATH, '//div[@id = "BackLink"]/a')
    IGUANA_BTN = (By.XPATH, '//div[@id="Catalog"]//tr//a[contains(@href, "RP-LI-02")]')
    IGUANA = (By.XPATH, '//div[@id = "Catalog"]//td[contains(., "RP-LI-02")]')
    GOLDFISH_BTN = (By.XPATH, '//div[@id="Catalog"]//td//a[contains(@href, "FI-SW-01")]')
    GOLDFISH_FEMALE = (By.XPATH, '//div[@id="Catalog"]//tr//td//a[contains(@href, "EST-21") and @class = "Button"]')



class CatalogPage(BasePage):
    def return_to_main_menu(self):
        self.click(Locators.RETURN_TO_MAIN_MENU)