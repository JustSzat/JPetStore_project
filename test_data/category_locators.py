from selenium.webdriver.common.by import By

CATEGORY_LOCATORS = {
    "Reptiles": (By.XPATH, '//*[@id="QuickLinks"]/a[3]'),
    "Fish": (By.XPATH, '//*[@id="QuickLinks"]/a[1]'),
    "Dogs": (By.XPATH, '//*[@id="QuickLinks"]/a[2]')



}