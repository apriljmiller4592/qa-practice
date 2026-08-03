from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

def test_open_google():

    #Arrange
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    try:
        # Act
        driver.get("https://www.google.com")

        # Assert
        assert "Google" in driver.title

    finally:
        driver.quit()