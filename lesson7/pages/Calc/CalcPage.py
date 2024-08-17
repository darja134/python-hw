from selenium.webdriver.common.by import By
from time import sleep
import unittest

class CalcPage:
    def __init__(self, driver): 
        self._driver = driver
        self._driver.maximize_window()
        self._driver.delete_all_cookies()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        self._driver.implicitly_wait(10)

    
    def set_delay(self, delay):
        # clear delay field and enter new delay
        delay_field = self._driver.find_element(By.CSS_SELECTOR, "input[id='delay']")
        delay_field.clear()
        delay_field.send_keys(delay)


    def press_calc_buttons(self, number1, sign, number2):
        # press calculator buttons
        self._driver.find_element(By.XPATH, "//span[contains(text(),'"+number1+"')]").click() # 7
        self._driver.find_element(By.XPATH, "//span[contains(text(),'"+sign+"')]").click() # +
        self._driver.find_element(By.XPATH, "//span[contains(text(),'"+number2+"')]").click() # 8
        self._driver.find_element(By.XPATH, "//span[contains(text(),'=')]").click() # =


    def wait_and_assert_result(self, delay, expected_result, assertion_message):
        # to use assertEqual
        tc = unittest.TestCase()
        
        sleep(delay)
        # get result
        real_result = self._driver.find_element(By.CSS_SELECTOR, "div[class='screen']").text
        # assert result is as axpected and quit browser
        tc.assertEqual(real_result, expected_result, assertion_message)
