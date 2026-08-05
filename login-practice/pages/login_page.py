from selenium.webdriver.common.by import By


class LoginPage:

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(
            "https://practicetestautomation.com/practice-test-login/"
        )

    def login(self, username, password):
        self.driver.find_element(*self.USERNAME).send_keys(username)
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        self.driver.find_element(*self.SUBMIT).click()