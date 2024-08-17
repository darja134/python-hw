from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from pages.Calc.CalcPage import CalcPage

# define delay
delay = 45
expected_result = '15'
assertion_message = "Result should be " + expected_result

def test_calculator():
    driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    calc_page = CalcPage(driver_firefox)

    calc_page.set_delay(delay)
    calc_page.press_calc_buttons('7', '+', '8')
    calc_page.wait_and_assert_result(delay, expected_result, assertion_message)

    driver_firefox.quit()