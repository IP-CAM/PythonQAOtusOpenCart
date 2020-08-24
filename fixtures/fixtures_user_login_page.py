import pytest
from selenium import webdriver

from pages.user_login_page import UserLoginPage


@pytest.fixture(scope="function")
def user_login_page(browser: webdriver, page_logging) -> UserLoginPage:
    user_login_page = UserLoginPage(driver=browser, logging_enabled=page_logging)
    user_login_page.open_page()
    return user_login_page
#
