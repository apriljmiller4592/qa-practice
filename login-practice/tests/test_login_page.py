from pages.login_page import LoginPage


def test_valid_login(driver):

    # Arrange
    page = LoginPage(driver)

    # Act
    page.open()
    page.login("student", "Password123")

    # Assert
    assert "Logged In Successfully" in driver.page_source