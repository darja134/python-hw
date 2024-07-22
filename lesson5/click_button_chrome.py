from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

n = 5 # how many times to click

driver_google = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_google.maximize_window()
driver_google.delete_all_cookies()

driver_google.get("http://the-internet.herokuapp.com/add_remove_elements/")
for i in range(0, n):
    driver_google.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()

deleteButtons = driver_google.find_elements(By.CSS_SELECTOR, "button[onclick='deleteElement()']")
print("Quantity of \"Delete\" buttons in Google Chrome is: " + str(len(deleteButtons)))
driver_google.quit()