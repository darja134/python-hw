from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
# next two imports for fluent wait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver_firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver_firefox.delete_all_cookies()

driver_firefox.get("http://the-internet.herokuapp.com/entry_ad")
driver_firefox.implicitly_wait(10)

#fluent wait (throws error "element not interactable")
#wait = WebDriverWait(driver_firefox, timeout=10, poll_frequency=5)
#wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[class='modal-footer']")))
driver_firefox.find_element(By.CSS_SELECTOR, "div[class='modal-footer']").click()
sleep(1) # to see modal dialog is closed
driver_firefox.quit()

# flaky, sometimes "Close" is not clicked