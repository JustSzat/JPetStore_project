from selenium.webdriver.common.by import By

PRODUCT_LOCATORS = {
    "Iguana": (By.XPATH, '//div[@id="Catalog"]//tr//a[contains(@href, "RP-LI-02")]'),
    "Goldfish": (By.XPATH, '//div[@id="Catalog"]//td//a[contains(@href, "FI-FW-02")]'),
    "Goldfish Female": (By.XPATH, '//div[@id="Catalog"]//tr//td//a[contains(@href, "EST-21") and @class = "Button"]'),
    "Poodle": (By.XPATH, '//div[@id = "Catalog"]//tr/td/a[contains(@href, "K9-PO-02")]')
}