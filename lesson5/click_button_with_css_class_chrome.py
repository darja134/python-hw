from time import sleep # only to see popup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver_google = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_google.maximize_window()
driver_google.delete_all_cookies()

driver_google.get("http://uitestingplayground.com/classattr")
driver_google.implicitly_wait(10)
driver_google.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]").click()
sleep(1) # to see popup "Primary button pressed"
driver_google.quit()

# throws error:
# handshake failed; returned -1, SSL error code 1, net_error -200