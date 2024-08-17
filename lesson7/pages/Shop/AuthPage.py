from selenium.webdriver.common.by import By

class AuthPage:

    def __init__(self, driver): 
        self._driver = driver
        self._driver.maximize_window()
        self._driver.delete_all_cookies()
        self._driver.get("https://www.saucedemo.com/")
        self._driver.implicitly_wait(10)

    
    def login(self, username, password):
        # login page (fill in fields + press button)
        self._driver.find_element(By.CSS_SELECTOR, "input[data-test='username']").send_keys(username)
        self._driver.find_element(By.CSS_SELECTOR, "input[data-test='password']").send_keys(password)
        self._driver.find_element(By.CSS_SELECTOR, "input[data-test='login-button']").click()
        self._driver.implicitly_wait(10)