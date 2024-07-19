from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_firefox.delete_all_cookies()

driver_firefox.get("http://uitestingplayground.com/dynamicid")
driver_firefox.implicitly_wait(10)
driver_firefox.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
driver_firefox.quit()