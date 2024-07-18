from time import sleep # only to see inputs!
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# next two imports for fluent wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

n = 5 # how many times to click

# GOOGLE CHROME
driver_google = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_google.maximize_window()
driver_google.delete_all_cookies()

# MODAL DIALOG (flaky)
driver_google.get("http://the-internet.herokuapp.com/entry_ad")
driver_google.implicitly_wait(10)

#fluent wait (throws error "element not interactable")
#wait = WebDriverWait(driver_google, timeout=10, poll_frequency=5)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='modal-footer']")))
driver_google.find_element(By.CSS_SELECTOR, "div[class='modal-footer']").click()


# CLICK BUTTON
driver_google.get("http://the-internet.herokuapp.com/add_remove_elements/")
for i in range(0, n):
    driver_google.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
deleteButtons = driver_google.find_elements(By.CSS_SELECTOR, "button[onclick='deleteElement()']")
print("Quantity of \"Delete\" buttons in Google Chrome is: " + str(len(deleteButtons)))


# CLICK BUTTON WITHOUT ID
driver_google.get("http://uitestingplayground.com/dynamicid")
driver_google.implicitly_wait(10)
driver_google.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()


# INPUT FIELD
driver_google.get("http://the-internet.herokuapp.com/inputs")
input_g = driver_google.find_element(By.CSS_SELECTOR, "input[type='number']")
input_g.send_keys("1000")
sleep(1) # to see input
input_g.clear()
input_g.send_keys("999")
sleep(1) # to see input


# FILL IN LOGIN FORM FIELDS AND LOGIN
driver_google.get("http://the-internet.herokuapp.com/login")
driver_google.find_element(By.ID, "username").send_keys("tomsmith")
driver_google.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver_google.find_element(By.CSS_SELECTOR, "i[class='fa fa-2x fa-sign-in']").click()


# CLICK BUTTON WITH CSS CLASS
driver_google.get("http://uitestingplayground.com/classattr")
driver_google.implicitly_wait(10)
driver_google.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]").click()
sleep(1) # to see popup "Primary button pressed"
driver_google.quit()


# FIREFOX
driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_firefox.delete_all_cookies()

# MODAL DIALOG (more stable when executed first)
driver_firefox.get("http://the-internet.herokuapp.com/entry_ad")
driver_firefox.implicitly_wait(10)

#fluent wait (throws error "element not interactable")
#wait = WebDriverWait(driver_firefox, timeout=10, poll_frequency=5)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='modal-footer']")))
driver_firefox.find_element(By.CSS_SELECTOR, "div[class='modal-footer']").click()


# CLICK BUTTON
driver_firefox.get("http://the-internet.herokuapp.com/add_remove_elements/")
for i in range(0, n):
    driver_firefox.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']").click()
deleteButtons = driver_firefox.find_elements(By.CSS_SELECTOR, "button[onclick='deleteElement()']")
print("Quantity of \"Delete\" buttons in Firefox is: " + str(len(deleteButtons)))


# CLICK BUTTON WITHOUT ID
driver_firefox.get("http://uitestingplayground.com/dynamicid")
driver_firefox.implicitly_wait(10)
driver_firefox.find_element(By.CSS_SELECTOR, "button[class='btn btn-primary']").click()


# INPUT FIELD
driver_firefox.get("http://the-internet.herokuapp.com/inputs")
input_f = driver_firefox.find_element(By.CSS_SELECTOR, "input[type='number']")
input_f.send_keys("1000")
sleep(1) # to see input
input_f.clear()
input_f.send_keys("999")
sleep(1) # to see input


# FILL IN LOGIN FORM FIELDS AND LOGIN
driver_firefox.get("http://the-internet.herokuapp.com/login")
driver_firefox.find_element(By.ID, "username").send_keys("tomsmith")
driver_firefox.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver_firefox.find_element(By.CSS_SELECTOR, "i[class='fa fa-2x fa-sign-in']").click()


# CLICK BUTTON WITH CSS CLASS
driver_firefox.get("http://uitestingplayground.com/classattr")
driver_firefox.implicitly_wait(10)
driver_firefox.find_element(By.XPATH, "//button[contains(@class, 'btn-primary')]").click()
sleep(1) # to see popup "Primary button pressed"
driver_firefox.quit()