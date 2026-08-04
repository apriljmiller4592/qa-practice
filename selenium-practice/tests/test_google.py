from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_open_google():

    #Arrange
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Act
        driver.get("https://the-internet.herokuapp.com")

        heading = driver.find_element(By.TAG_NAME, "h1")

        # Assert
        assert heading.text == "Welcome to the-internet"

    finally:
        driver.quit()