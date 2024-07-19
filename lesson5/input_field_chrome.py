from time import sleep # only to see inputs!
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver_google = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_google.maximize_window()
driver_google.delete_all_cookies()

driver_google.get("http://the-internet.herokuapp.com/inputs")
input_g = driver_google.find_element(By.CSS_SELECTOR, "input[type='number']")
input_g.send_keys("1000")
sleep(1) # to see input
input_g.clear()
input_g.send_keys("999")
sleep(1) # to see input
driver_google.quit()