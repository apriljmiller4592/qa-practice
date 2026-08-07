from pages.login_page import LoginPage

# Test that a valid user can login successfully
def test_valid_login(driver):

    # Arrange
    # Create a login page object and give it the browser
    page = LoginPage(driver)

    # Act
    # Open the login page
    page.open()

    # Enter valid credentials and submit
    page.login("student", "Password123")

    # Assert
    # Verify that login was successful
    assert page.success_message() == "Logged In Successfully"

# Test that the login page has the correct title
def test_login_page_title(driver):
    # Arrange
    page = LoginPage(driver)

    # Act 
    page.open()

    #Assert 
    assert "Test Login" in page.get_title()

def test_invalid_password(driver):

    # Arrange
    page = LoginPage(driver)

    # Act
    page.open()

    page.login(
        "student",
        "wrongpassword"
    )

    # Assert
    assert page.get_error_message() == (
        "Your password is invalid!"
    )
