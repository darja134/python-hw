from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

n = 5 # how many times to click

driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_firefox.delete_all_cookies()

driver_firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")
for i in range(0, n):
    driver_firefox.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()

deleteButtons = driver_firefox.find_elements(By.CSS_SELECTOR, "button[onclick='deleteElement()']")
print("Quantity of \"Delete\" buttons in Firefox is: " + str(len(deleteButtons)))
driver_firefox.quit()