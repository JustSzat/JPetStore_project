import re

import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import home_page, catalog_page
from pages.base_page import BasePage
from pages.catalog_page import Locators
from test_data.product_locators import PRODUCT_LOCATORS


class Locators:

    UPDATE_CARD_BTN = (By.XPATH, '//div[@id = "Cart"]//table//td/input[@value = "Update Cart"]')
    ICON_CART = (By.XPATH, '//div[@id = "MenuContent"]/a[contains(@href, "Cart.action")]')
    REMOVE_BTN = (By.XPATH, '//div[@id ="Cart"]//tr//td//a[@class = "Button" and contains(text(), "Remove")]')
    MESSAGE_EMPTY_CARD = (By.XPATH, '//div[@id="Cart"]//table//b[contains(text(), "Your cart is empty")]')
    ADDED_ITEMS = (By.XPATH, '//div[@id = "Cart"]//table//tr[position() > 1 and position() < last()]')
    ADD_TO_CART_BTN = (By.XPATH, '//div[@id = "Catalog"]//td/a[@class = "Button" and contains(text(), "Add to Cart")]')
    EMPTY_CARD = (By.XPATH,'//div[@id="Cart"]//tr/td/b[contains(text(), "Your cart is empty")]')
    TOTAL_PRICE = (By.XPATH, '//div[@id = "Cart"]//tr/td[contains(text(), "Total")]')
    ITEM_PRICES = (By.XPATH, '//div[@id="Cart"]//tr[position()>1 and position()<last()]//td[7]')

class CartPage(BasePage):

    def add_item(self, product):


        if "Female" in product:
            goldfish_locator = PRODUCT_LOCATORS.get("Goldfish")
            self.click(goldfish_locator)
            female_goldfish_locator = PRODUCT_LOCATORS.get("Goldfish Female")
            self.click(female_goldfish_locator)
        else:
            locator = PRODUCT_LOCATORS.get(product)
            self.click(locator)
            self.click_add_to_cart()

    def click_add_to_cart(self):
        self.click(Locators.ADD_TO_CART_BTN)

    def enter_to_cart(self):
        self.click(Locators.ICON_CART)

    def get_empty_cart_message(self):
        WebDriverWait(self.driver,10).until_not(EC.presence_of_element_located(Locators.REMOVE_BTN))
        message = self.find(Locators.MESSAGE_EMPTY_CARD)
        return message.text

    def get_items_prices(self):
        added_items_price = self.find_all(Locators.ITEM_PRICES)
        prices = []
        for price in added_items_price:
            price_text = price.text
            print(repr(price_text))

            price = float(price_text.replace("$", "").strip())
            prices.append(price)
        return prices


    def get_total_price(self):
        total_price = self.find(Locators.TOTAL_PRICE)
        total_price_text = total_price.text
        print(repr(total_price_text))
        return float(total_price_text.replace("Sub Total: $", "").strip())

    def open_reptiles(self):
        self.click(home_page.Locators.QUICKLINK_REPTILES)

    def open_fish(self):
        self.click(home_page.Locators.QUICKLINK_FISH)

    def get_reptiles_list(self):
        reptiles = self.find_all(home_page.Locators.FOUND_REPTILES)
        reptiles_list = []
        for rep in reptiles:
            reptiles_list.append(rep.text)
        return reptiles_list

    def get_shopping_cart_list(self):
        added_items = self.find_all(Locators.ADDED_ITEMS)
        cart_list = []
        for item in added_items:
            cart_list.append(item.text)
        print(cart_list)
        return cart_list

    def get_shopping_cart_list_not_string(self):
        added_items = self.find_all(Locators)
        cart_list =[
            {"code": "RP-LI-02", "price": 18.50, "qty": 1},
            {"code": "FI-FW-01", "price": 10.00, "qty": 1}
        ]


    def remove_item(self):
        self.click(Locators.REMOVE_BTN)










