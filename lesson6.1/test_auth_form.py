from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
import pytest
import unittest

# define expected color and assertion message
expected_color = '#f8d7da'
assertion_message = 'Color is not ' + expected_color

@pytest.mark.parametrize('expected_color, assertion_message', [(expected_color, assertion_message)])
def test_auth(expected_color, assertion_message):
    # to use assertions outside of a class
    tc = unittest.TestCase()

    driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver_firefox.maximize_window()
    driver_firefox.delete_all_cookies()
    driver_firefox.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    driver_firefox.implicitly_wait(10)

    # form fields
    first_name_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys("Иван")
    last_name_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys("Петров")
    address_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys("Ленина, 55-3")
    email_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys("test@skypro.com")
    phone_number_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys("+7985899998787")
    city_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys("Москва")
    country_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys("Россия")
    job_position_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys("QA")
    company_field = driver_firefox.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys("SkyPro")

    # "Submit" button
    driver_firefox.find_element(By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']").click()
    driver_firefox.implicitly_wait(10)

    # get field property backgroud-color and convert to hex
    zip_code_field = driver_firefox.find_element(By.CSS_SELECTOR, "div[id='zip-code']")
    real_color = zip_code_field.value_of_css_property("background-color")
    real_color = Color.from_string(real_color).hex

    # assert color is as axpected and quit browser
    tc.assertEqual(real_color, expected_color, assertion_message)
    driver_firefox.quit()