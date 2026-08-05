from selenium.webdriver.common.by import By
from pages.base_page import BasePage

# LoginPage represents the login page and inherits all methods from BasePage
class LoginPage(BasePage):

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "submit")

    SUCCESS_MESSAGE = (By.TAG_NAME, "h1")

    # Open the login page
    def open(self):
        self.driver.get(
            "https://practicetestautomation.com/practice-test-login/"
        )

    # Performs the login action
    # 1. Enter username
    # 2. Enter password
    # 3. Click login    
    def login(self, username, password):
        self.type(
            self.USERNAME,
            username
        )

        self.type(
            self.PASSWORD,
            password
        )

        self.click(
            self.SUBMIT
        )

    # Gets the success message after login
    def success_message(self):
        return self.get_text(
            self.SUCCESS_MESSAGE
        )