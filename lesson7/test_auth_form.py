from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from define_class.Form import Form
from pages.Auth.AuthPage import AuthPage

form_fields = Form("Иван", "Петров", "Ленина, 55-3", "test@skypro.com", "+7985899998787", \
                   "Москва", "Россия", "QA", "SkyPro")

# define expected color and assertion message
expected_color_zip = '#f8d7da'
assertion_message_zip = 'Color is not ' + expected_color_zip
expected_color_other = '#d1e7dd'
assertion_message_other = 'Color is not ' + expected_color_other

def test_auth_with_zip_field_empty(): 
    driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    auth_page = AuthPage(driver_firefox)

    auth_page.fill_form(form_fields)
    auth_page.press_submit()
    auth_page.assert_zip_field_is_red(expected_color_zip, assertion_message_zip)
    auth_page.assert_other_fields_are_green(expected_color_other, assertion_message_other)

    driver_firefox.quit()
