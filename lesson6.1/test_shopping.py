from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
import pytest
import unittest

# definition of 
expected_total = '58.29'
assertion_message = 'Total should be ' + expected_total

@pytest.mark.parametrize('expected_total, assertion_message', [(expected_total, assertion_message)])
def test_shopping(expected_total, assertion_message):
    # to use assertions outside of a class
    tc = unittest.TestCase()

    driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver_firefox.maximize_window()
    driver_firefox.delete_all_cookies()
    driver_firefox.get("https://www.saucedemo.com/")
    driver_firefox.implicitly_wait(10)

    # login page (fill in fields + press button)
    driver_firefox.find_element(By.CSS_SELECTOR, "input[data-test='username']").send_keys("standard_user")
    driver_firefox.find_element(By.CSS_SELECTOR, "input[data-test='password']").send_keys("secret_sauce")
    driver_firefox.find_element(By.CSS_SELECTOR, "input[data-test='login-button']").click()

    # find items and add to cart
    driver_firefox.implicitly_wait(10)
    backpack_button_xpath = "//*[contains(text(), 'Sauce Labs Backpack')]/parent::a/parent::div/following-sibling::div/child::button"
    driver_firefox.find_element(By.XPATH, backpack_button_xpath).click()
    tshirt_button_xpath = "//*[contains(text(), 'Sauce Labs Bolt T-Shirt')]/parent::a/parent::div/following-sibling::div/child::button"
    driver_firefox.find_element(By.XPATH, tshirt_button_xpath).click()
    onesie_button_xpath = "//*[contains(text(), 'Sauce Labs Onesie')]/parent::a/parent::div/following-sibling::div/child::button"
    driver_firefox.find_element(By.XPATH, onesie_button_xpath).click()

    # click shopping cart icon
    driver_firefox.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()

    # click checkout button
    driver_firefox.find_element(By.CSS_SELECTOR, "button[data-test='checkout']").click()

    # checkout page (fill in fields + press button)
    driver_firefox.find_element(By.CSS_SELECTOR, "input[data-test='firstName']").send_keys("Иван")
    driver_firefox.find_element(By.CSS_SELECTOR, "input[data-test='lastName']").send_keys("Петров")
    driver_firefox.find_element(By.CSS_SELECTOR, "input[data-test='postalCode']").send_keys("000000")
    driver_firefox.find_element(By.CSS_SELECTOR, "input[data-test='continue']").click()

    # get total from page
    driver_firefox.implicitly_wait(10)
    real_total = driver_firefox.find_element(By.CSS_SELECTOR, "div[data-test='total-label']").text

    # assert total is as axpected and quit browser
    tc.assertEqual(real_total[-5:], expected_total, assertion_message)
    driver_firefox.quit()