from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_firefox.delete_all_cookies()

driver_firefox.get("http://the-internet.herokuapp.com/login")
driver_firefox.find_element(By.ID, "username").send_keys("tomsmith")
driver_firefox.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver_firefox.find_element(By.CSS_SELECTOR, "i[class='fa fa-2x fa-sign-in']").click()
driver_firefox.quit()