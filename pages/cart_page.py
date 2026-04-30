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

class CartPage(BasePage):

    def enter_to_cart(self):
        icon_cart = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.ICON_CART))
        icon_cart.click()

    def get_message_empty_cart(self):
        message = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//div[@id="Cart"]//table//b[contains(text(), "Your cart is empty")]')))
        return message
    def add_to_the_cart(self):
        reptiles = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(home_page.Locators.QUICKLINK_REPTILES))
        reptiles.click()
        found_reptiles = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@id="Catalog"]//tr[position() > 1] ')))
        reptiles_list = []
        for rep in found_reptiles:
            reptiles_list.append(rep.text)
        return reptiles_list

    def add_to_the_cart_fish(self):
        fish = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(home_page.Locators.QUICKLINK_FISH))
        fish.click()
        found_fish = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@id="Catalog"]//tr[position() > 1] ')))
        fish_list = []
        for rep in found_fish:
            fish_list.append(rep.text)
        return fish_list

    def get_shopping_cart_list(self):
        added_items = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located((By.XPATH, '//div[@id = "Cart"]//table//tr[position() > 1 and position() < last()]')))
        cart_list = []
        for item in added_items:
            cart_list.append(item.text)
        print(cart_list)
        return cart_list
    def get_shopping_cart_list_not_string(self):
        added_items = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(
            (By.XPATH, '//div[@id = "Cart"]//table//tr[position() > 1 and position() < last()]')))
        cart_list =[
            {"code": "RP-LI-02", "price": 18.50, "qty": 1},
            {"code": "FI-FW-01", "price": 10.00, "qty": 1}
        ]


    def remove_item(self):
        remove_btn = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(Locators.REMOVE_BTN))
        remove_btn.click()










