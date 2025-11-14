import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize("username, password, expected_error", [
    ("", "123456", "Epic sadface: Username is required"),
    ("user", "", "Epic sadface: Password is required"),
    ("locked_out_user", "secret_sauce", "Epic sadface: Sorry, this user has been locked out."),
])
def test_login_negative(driver, username, password, expected_error):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    error_text = login_page.get_text(LoginPage.ERROR_MSG)
    assert expected_error == error_text


@pytest.mark.parametrize("username, password, expected_information", [
    ("standard_user", "secret_sauce", ""),
])
def test_login_positive(driver, username, password, expected_information):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(username, password)
    assert expected_information in driver.page_source
