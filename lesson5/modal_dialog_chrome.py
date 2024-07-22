from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
# next two imports for fluent wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_google = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_google.maximize_window()
driver_google.delete_all_cookies()

driver_google.get("http://the-internet.herokuapp.com/entry_ad")
driver_google.implicitly_wait(10)

#fluent wait (throws error "element not interactable")
#wait = WebDriverWait(driver_google, timeout=10, poll_frequency=5)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='modal-footer']")))
driver_google.find_element(By.CSS_SELECTOR, "div[class='modal-footer']").click()
sleep(1) # to see modal dialog is closed
driver_google.quit()