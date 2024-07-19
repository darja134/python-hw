from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver_google = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_google.maximize_window()
driver_google.delete_all_cookies()

driver_google.get("http://the-internet.herokuapp.com/login")
driver_google.find_element(By.ID, "username").send_keys("tomsmith")
driver_google.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver_google.find_element(By.CSS_SELECTOR, "i[class='fa fa-2x fa-sign-in']").click()
driver_google.quit()