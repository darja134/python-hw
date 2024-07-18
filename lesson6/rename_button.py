from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver_google = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_google.maximize_window()
driver_google.delete_all_cookies()
driver_google.get("http://uitestingplayground.com/textinput")
driver_google.find_element(By.CSS_SELECTOR, "input[class='form-control']").send_keys("SkyPro")
driver_google.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()
driver_google.implicitly_wait(10) # what's common timeout?
element = driver_google.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']")
print(element.text)