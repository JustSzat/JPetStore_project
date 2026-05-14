
print("----- DEBUG -----")
print("PRODUCT RAW:", repr(product))
product = product.strip()
print("PRODUCT CLEAN:", repr(product))
print("AVAILABLE KEYS:", [repr(k) for k in PRODUCT_LOCATORS.keys()])
locator = PRODUCT_LOCATORS.get(product)
print("LOCATOR:", locator)
print("------------------")
