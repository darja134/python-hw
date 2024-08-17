from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.Shop.AuthPage import AuthPage
from pages.Shop.ShopPage import ShopPage
from pages.Shop.CartPage import CartPage
from pages.Shop.CheckoutPage import CheckoutPage


# definition of sum
expected_total = '58.29'
assertion_message = 'Total should be ' + expected_total

def test_shopping():

    driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    auth_page = AuthPage(driver_firefox)
    auth_page.login("standard_user", "secret_sauce")

    shop_page = ShopPage(driver_firefox)
    shop_page.add_to_cart('backpack', 'bolt-t-shirt', 'onesie')
    shop_page.press_shopping_cart_button()

    cart_page = CartPage(driver_firefox)
    cart_page.press_checkout_button()

    checkout_page = CheckoutPage(driver_firefox)
    checkout_page.fill_checkout_fields_and_press_button("Иван", "Петров", "000000")
    checkout_page.get_and_assert_total(expected_total, assertion_message)

    driver_firefox.quit()