from time import sleep # only to see inputs!
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_firefox.delete_all_cookies()

driver_firefox.get("http://the-internet.herokuapp.com/inputs")
input_f = driver_firefox.find_element(By.CSS_SELECTOR, "input[type='number']")
input_f.send_keys("1000")
sleep(1) # to see input
input_f.clear()
input_f.send_keys("999")
sleep(1) # to see input
driver_firefox.quit()