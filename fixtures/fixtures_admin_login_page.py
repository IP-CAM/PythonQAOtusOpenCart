import pytest
from selenium import webdriver

from pages.admin_login_page import AdminLoginPage


@pytest.fixture(scope="function")
def admin_login_page(browser: webdriver, page_logging: bool) -> AdminLoginPage:
    admin_login_page = AdminLoginPage(driver=browser, logging_enabled=page_logging)
    admin_login_page.open_page()
    return admin_login_page
#
