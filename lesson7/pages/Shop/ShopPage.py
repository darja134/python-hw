from selenium.webdriver.common.by import By

class ShopPage:

    def __init__(self, browser):
        self._driver = browser


    def add_to_cart(self, item1, item2, item3):
        self._driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-"+item1+"']").click()
        self._driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-"+item2+"']").click()
        self._driver.find_element(By.CSS_SELECTOR, "button[data-test='add-to-cart-sauce-labs-"+item3+"']").click()


    def press_shopping_cart_button(self):
        self._driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()
