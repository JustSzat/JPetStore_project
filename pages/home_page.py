from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage


class HomePage(BasePage):

    def click_enter_the_store(self):
        enter_click = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, "Content")))
        enter_click.click()
