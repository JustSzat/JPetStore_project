from decimal import Decimal

import mysql.connector

from test_cases.base_test import BaseTest


class TestOrderTotals(BaseTest):
    def get_test_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="myuser",
            password="mypass",
            database="jpetstore"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT product_id, quantity, expected_total * FROM order_test_case")

        data = cursor.fetchall()
        conn.close()
        return data

    def calculate_total(self, product_id, quantity):
        price = Decimal("18.00")
        return price * Decimal(quantity)
    def test_order_totals(self):
        for product_id, quantity, expected in self.get_test_data():
            result = self.calculate_total(product_id, quantity)
            self.assertEqual(result, expected, f"Blad dla prod {product_id}")