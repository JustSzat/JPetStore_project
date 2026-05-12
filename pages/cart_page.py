import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import home_page
from pages.base_page import BasePage
from test_cases import cart_test


class Locators:
    UPDATE_CARD_BTN = (By.XPATH, '//div[@id = "Cart"]//table//td/input[@value = "Update Cart"]')
    ICON_CART = (By.XPATH, '//div[@id = "MenuContent"]/a[contains(@href, "Cart.action")]')
    REMOVE_BTN = (By.XPATH, '//div[@id ="Cart"]//tr//td//a[@class = "Button" and contains(text(), "Remove")]')
    MESSAGE_EMPTY_CARD = (By.XPATH, '//div[@id="Cart"]//table//b[contains(text(), "Your cart is empty")]')
    ADDED_ITEMS = (By.XPATH, '//div[@id = "Cart"]//table//tr[position() > 1 and position() < last()]')

class CartPage(BasePage):

    def enter_to_cart(self):
        self.click(Locators.ICON_CART)

    def get_message_empty_cart(self):
        message = self.find_element_located(Locators.MESSAGE_EMPTY_CARD)
        return message

    def add_to_the_cart(self):
        self.click(home_page.Locators.QUICKLINK_REPTILES)
        found_reptiles = self.visible_all_elements_located(home_page.Locators.FOUND_REPTILES)
        reptiles_list = []
        for rep in found_reptiles:
            reptiles_list.append(rep.text)
        return reptiles_list

    def add_to_the_cart_fish(self):
        self.click(home_page.Locators.QUICKLINK_FISH)
        found_fish = self.visible_all_elements_located(home_page.Locators.FOUND_FISH)
        fish_list = []
        for rep in found_fish:
            fish_list.append(rep.text)
        return fish_list

    def get_shopping_cart_list(self):
        added_items = self.visible_all_elements_located(Locators.ADDED_ITEMS)
        cart_list = []
        for item in added_items:
            cart_list.append(item.text)
        print(cart_list)
        return cart_list

    def get_shopping_cart_list_not_string(self):
        added_items = self.visible_all_elements_located(Locators)
        cart_list =[
            {"code": "RP-LI-02", "price": 18.50, "qty": 1},
            {"code": "FI-FW-01", "price": 10.00, "qty": 1}
        ]


    def remove_item(self):
        self.click(Locators.REMOVE_BTN)










