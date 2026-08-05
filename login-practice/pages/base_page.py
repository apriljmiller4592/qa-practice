from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# BasePage contains reusable actions every page can use
class BasePage:

    # Constructor runs when a page object is created
    def __init__(self, driver):
        self.driver = driver
        # Use explicit wait and wait for 10 seconds for elements to appear
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator):
        # Wait until element is visible and clickable
        element = self.wait.until(
            EC.element_to_be_clickable(locator)
        )

        # Click the element
        element.click()

    # Reusable method for typing into text fields
    def type(self, locator, text):
        # Wait until the text box is visible
        element = self.wait.until(
            EC.visibility_of_element_located(locator)
        )

        # Clear anything already in the field
        element.clear()

        # Type into the text box with the provided text
        element.send_keys(text)

    # Return the title of the current browser page
    def get_title(self):
        return self.driver.title

    # Return the current URL
    def current_url(self):
        return self.driver.current_url
    