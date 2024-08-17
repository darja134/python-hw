from selenium.webdriver.common.by import By
import unittest

class CheckoutPage:

    def __init__(self, browser):
        self._driver = browser


    def fill_checkout_fields_and_press_button(self, first_name, last_name, postal_code):
        self._driver.find_element(By.CSS_SELECTOR, "input[data-test='firstName']").send_keys(first_name)
        self._driver.find_element(By.CSS_SELECTOR, "input[data-test='lastName']").send_keys(last_name)
        self._driver.find_element(By.CSS_SELECTOR, "input[data-test='postalCode']").send_keys(postal_code)
        self._driver.find_element(By.CSS_SELECTOR, "input[data-test='continue']").click()
        self._driver.implicitly_wait(10)


    def get_and_assert_total(self, expected_total, assertion_message):
        # to use assertEqual
        tc = unittest.TestCase()
        # get total from page
        real_total = self._driver.find_element(By.CSS_SELECTOR, "div[data-test='total-label']").text
        # assert total is as axpected and quit browser
        tc.assertEqual(real_total[-5:], expected_total, assertion_message)