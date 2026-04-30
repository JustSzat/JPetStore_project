from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import catalog_page, cart_page, home_page
from pages.cart_page import CartPage
from pages.catalog_page import Locators
from pages.home_page import HomePage
from test_cases.base_test import BaseTest


class CartTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.home_page.click_enter_the_store()
        self.cart_page = CartPage(self.driver)

    def test_empty_cart_message(self):
        self.cart_page.enter_to_cart()
        message = self.cart_page.get_message_empty_cart()
        print(message.text)
        self.assertIn("Your cart is empty", message.text)

    def test_adding_to_cart(self):
        """
        Test, ktory sprawdza czy dodany produkt jest w koszyku
        """
        self.cart_page.add_to_the_cart()
        iguana_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(catalog_page.Locators.IGUANA_BTN))
        iguana_btn.click()
        add_to_cart = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@id = "Catalog"]//td/a[@class = "Button" and contains(text(), "Add to Cart")]')))
        add_to_cart.click()
        cart_list = self.cart_page.get_shopping_cart_list()
        iguana_text = self.driver.find_element(*Locators.IGUANA).text
        self.assertTrue(
            any(iguana_text in item for item in cart_list)
        )
    def test_remove_item_message(self):
        """
        Usuwanie produktu z koszyka
        """
        self.cart_page.add_to_the_cart()
        iguana_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(catalog_page.Locators.IGUANA_BTN))
        iguana_btn.click()
        add_to_cart = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@id = "Catalog"]//td/a[@class = "Button" and contains(text(), "Add to Cart")]')))
        add_to_cart.click()
        self.cart_page.remove_item()
        empty_cart = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH,'//div[@id="Cart"]//tr/td/b[contains(text(), "Your cart is empty")]')))
        self.assertIn("Your cart is empty", empty_cart.text)

    def test_remove_item(self):
        self.cart_page.add_to_the_cart()
        iguana_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(catalog_page.Locators.IGUANA_BTN))
        iguana_btn.click()
        add_to_cart = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//div[@id = "Catalog"]//td/a[@class = "Button" and contains(text(), "Add to Cart")]')))
        add_to_cart.click()
        self.cart_page.remove_item()
        cart_list = self.cart_page.get_shopping_cart_list()
        self.assertNotIn("RP-LI-02", " ".join(cart_list))

    def test_total_price(self):
        self.cart_page.add_to_the_cart()
        iguana_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(catalog_page.Locators.IGUANA_BTN))
        iguana_btn.click()
        fish_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(home_page.Locators.QUICKLINK_FISH))
        fish_btn.click()
        self.cart_page.add_to_the_cart_fish()
        goldfish_btn = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(catalog_page.Locators.GOLDFISH_BTN))
        goldfish_btn.click()
        goldfish_female = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(catalog_page.Locators.GOLDFISH_FEMALE))
        goldfish_female.click()
        cart_list = self.cart_page.get_shopping_cart_list()
        
















