from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver_google = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver_google.maximize_window()
driver_google.delete_all_cookies()
driver_google.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
text = ""
while text != "Done!":
    driver_google.implicitly_wait(2)
    element = driver_google.find_element(By.ID, "text")
    text = element.text
image_element = driver_google.find_element(By.ID, "award")
print(image_element.get_attribute("src"))