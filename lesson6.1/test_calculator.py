from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
import pytest
import unittest

# define delay
delay = 45
expected_result = '15'
assertion_message = "Result should be " + expected_result

@pytest.mark.parametrize('delay, expected_result, assertion_message', [(delay, expected_result, assertion_message)])
def test_calculator(delay, expected_result, assertion_message):
    # to use assertions outside of a class
    tc = unittest.TestCase()

    driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver_firefox.maximize_window()
    driver_firefox.delete_all_cookies()
    driver_firefox.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    driver_firefox.implicitly_wait(10)

    # clear delay field and enter new delay
    delay_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[id='delay']")
    delay_field.clear()
    delay_field.send_keys(delay)

    # press calculator buttons
    driver_firefox.find_element(By.XPATH, "//span[contains(text(),'7')]").click() # 7
    driver_firefox.find_element(By.XPATH, "//span[contains(text(),'+')]").click() # +
    driver_firefox.find_element(By.XPATH, "//span[contains(text(),'8')]").click() # 8
    driver_firefox.find_element(By.XPATH, "//span[contains(text(),'=')]").click() # =

    #WebDriverWait(driver_firefox, delay)
    sleep(delay)

    # get result
    real_result = driver_firefox.find_element(By.CSS_SELECTOR, "div[class='screen']").text

    # assert result is as axpected and quit browser
    tc.assertEqual(real_result, expected_result, assertion_message)
    driver_firefox.quit()