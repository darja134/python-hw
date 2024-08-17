from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color
from define_class.Form import Form
import unittest

class AuthPage:
    
    def __init__(self, driver): 
        self._driver = driver
        self._driver.maximize_window()
        self._driver.delete_all_cookies()
        self._driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
        self._driver.implicitly_wait(10)

    def fill_form(self, form_fields: Form):
        self._driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(form_fields.first_name)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(form_fields.last_name)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(form_fields.address)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(form_fields.email)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(form_fields.phone_number)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(form_fields.city)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(form_fields.country)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(form_fields.job_position)
        self._driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(form_fields.company)


    def press_submit(self):
        self._driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-outline-primary mt-3']").click()
        self._driver.implicitly_wait(10)

    
    def assert_zip_field_is_red(self, expected_color, assertion_message):
        # to use assertEqual
        tc = unittest.TestCase()

        # get field property backgroud-color and convert to hex
        zip_code_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='zip-code']")
        real_color_of_zip = AuthPage.get_color(zip_code_field)
        # assert color is as axpected
        tc.assertEqual(real_color_of_zip, expected_color, assertion_message)


    def assert_other_fields_are_green(self, expected_color, assertion_message):
        # to use assertEqual
        tc = unittest.TestCase()

        # assert color of first name field
        first_name_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='first-name']")
        real_color_of_fn = AuthPage.get_color(first_name_field)
        tc.assertEqual(real_color_of_fn, expected_color, assertion_message + ", first name field")

        # assert color of last name field
        last_name_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='last-name']")
        real_color_of_ln = AuthPage.get_color(last_name_field)
        tc.assertEqual(real_color_of_ln, expected_color, assertion_message + ", last name field")

        # assert color of address field
        address_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='address']")
        real_color_of_a = AuthPage.get_color(address_field)
        tc.assertEqual(real_color_of_a, expected_color, assertion_message + ", address field")

        # assert color of city field
        city_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='city']")
        real_color_of_city = AuthPage.get_color(city_field)
        tc.assertEqual(real_color_of_city, expected_color, assertion_message + ", city field")

        # assert color of country field
        country_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='country']")
        real_color_of_country = AuthPage.get_color(country_field)
        tc.assertEqual(real_color_of_country, expected_color, assertion_message + ", country field")

        # assert color of e-mail field
        email_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='e-mail']")
        real_color_of_e = AuthPage.get_color(email_field)
        tc.assertEqual(real_color_of_e, expected_color, assertion_message + ", e-mail field")

        # assert color of phone field
        phone_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='phone']")
        real_color_of_p = AuthPage.get_color(phone_field)
        tc.assertEqual(real_color_of_p, expected_color, assertion_message + ", phone field")

        # assert color of job-position field
        jobposition_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='job-position']")
        real_color_of_jp = AuthPage.get_color(jobposition_field)
        tc.assertEqual(real_color_of_jp, expected_color, assertion_message + ", job-position field")

        # assert color of company field
        company_field = self._driver.find_element(By.CSS_SELECTOR, "div[id='company']")
        real_color_of_company = AuthPage.get_color(company_field)
        tc.assertEqual(real_color_of_company, expected_color, assertion_message + ", company field")


    def get_color(field: WebElement):
        real_color = field.value_of_css_property("background-color")
        real_color = Color.from_string(real_color).hex
        return real_color