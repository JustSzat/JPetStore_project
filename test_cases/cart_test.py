import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages import cart_page, catalog_page
from pages.cart_page import CartPage
from pages.catalog_page import Locators, CatalogPage
from pages.home_page import HomePage
from test_cases.base_test import BaseTest
from test_data.store_items import load_data


class CartTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.home_page = HomePage(self.driver)
        self.home_page.click_enter_the_store()
        self.cart_page = CartPage(self.driver)
        self.catalog_page = CatalogPage(self.driver)


    def test_added_items_are_visible_in_cart(self):
        """
        Add items and check their visibility in cart
        """
        data = load_data("test_data/data_search.csv")

        added_items = []
        for category, product in data:
            print(f"Added: {product}")
            self.home_page.open_category(category)
            self.cart_page.add_item(product)
            added_items.append(product)

        cart_list = self.cart_page.get_shopping_cart_list()
        print(f"Cart list: {cart_list}")

        for product in added_items:
            self.assertIn(product,"".join(cart_list))

    def test_remove_item_and_check_empty_card(self):
        """
        Remove items from cart and check if "Your cart is empty" is displayed
        """
        data = load_data("test_data/data_search.csv")

        for category, product in data:
            print(f"Added: {product} from {category}")

            self.home_page.open_category(category)
            self.cart_page.add_item(product)

        for i in range(len(data)):
            self.cart_page.remove_item()

        message = self.cart_page.get_empty_cart_message()
        self.assertIn("Your cart is empty", message)

    def test_add_products_and_check_count(self):
        """
        Checking that number of products in cart matches expected count
        """
        # loading data from CSV
        data = load_data("test_data/data_search.csv")
        # select two products
        products_to_add = data[:2]
        # add products to cart
        for category, product in products_to_add:

            print(f"Added: {product} from {category}")

            self.home_page.open_category(category)
            self.cart_page.add_item(product)
        # get list of products in cart
        cart_items = self.cart_page.get_shopping_cart_list()
        # check number of products in cart
        self.assertEqual(print(len(cart_items)), print(len(products_to_add)))

    def test_add_items_and_verify_total_price(self):
        """
        Test of verification of total price in the cart
        """
        data = load_data("test_data/data_search.csv")

        for category, product in data:
            print(f"Added: {product} from {category}")
            self.home_page.open_category(category)
            self.cart_page.add_item(product)

        total_price = self.cart_page.get_total_price()
        item_added_price = self.cart_page.get_items_prices()
        self.assertEqual(total_price, sum(item_added_price))



if __name__=="__main__":
    import unittest
    unittest.main(verbosity=2)
















