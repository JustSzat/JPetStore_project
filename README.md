Traceback (most recent call last):
  File "/usr/lib/python3.12/unittest/loader.py", line 137, in loadTestsFromName
    module = __import__(module_name)
             ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/student/Desktop/Repozytoria/JPetStore_project/test_cases/cart_test.py", line 7, in <module>
    from pages import catalog_page, cart_page, home_page
  File "/home/student/Desktop/Repozytoria/JPetStore_project/pages/catalog_page.py", line 5, in <module>
    from pages import home_page
  File "/home/student/Desktop/Repozytoria/JPetStore_project/pages/home_page.py", line 11, in <module>
    from pages.catalog_page import CatalogPage
ImportError: cannot import name 'CatalogPage' from partially initialized module 'pages.catalog_page' (most likely due to a circular import) (/home/student/Desktop/Repozytoria/JPetStore_project/pages/catalog_page.py)
