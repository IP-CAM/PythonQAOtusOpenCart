import allure
import pytest

from configuration import (
    OPENCART_ADMIN_USERNAME,
    OPENCART_ADMIN_PASSWORD
)
from pages.administration_page import AdministrationPage


class TestAdminLoginPage:
    @allure.title("Check logo image")
    @allure.feature("Check elements before logging in")
    @allure.story("Logo")
    def test_header_logo(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.IMG_LOGO)
    #

    @allure.title("Negative check for logo image ")
    @allure.feature("Check elements before logging in")
    @allure.story("Logo")
    @pytest.mark.xfail
    def test_header_logo_negative(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.IMG_LOGO_NONEXISTENT)

    #

    @allure.title("Check username input label")
    @allure.feature("Check elements before logging in")
    @allure.story("Labels")
    def test_username_label(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.LABEL_FOR_USERNAME)
    #

    @allure.title("Check restore forgotten password link by XPath")
    @allure.feature("Check elements before logging in")
    @allure.story("Links")
    def test_forgotten_password_link(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.A_FORGOTTEN_PASSWORD)
    #

    @allure.title('Check "Please enter your login details." heading')
    @allure.feature("Check elements before logging in")
    @allure.story("Labels")
    def test_panel_heading(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.DIV_PANEL_HEADING)
    #

    @allure.title("Check OpenCart hyperlink")
    @allure.feature("Check elements before logging in")
    @allure.story("Links")
    def test_opencart_link(self, admin_login_page):
        assert admin_login_page.find_element(locator=admin_login_page.A_OPENCART)
    #

    @allure.title("Log in to administration page and then log out")
    @allure.feature("Check elements after logging in")
    @allure.story("Links")
    @pytest.mark.slow
    def test_login_logout(self, admin_login_page, browser, page_logging):

        with allure.step("Log in to administration page"):
            admin_login_page.log_in(
                username=OPENCART_ADMIN_USERNAME,
                password=OPENCART_ADMIN_PASSWORD
            )
        with allure.step("Check administration page"):
            administration_page = AdministrationPage(driver=browser, logging_enabled=page_logging)
            assert administration_page.find_element(locator=administration_page.DIV_DASHBOARD)

        with allure.step("Log out"):
            administration_page.log_out()

    #
#
