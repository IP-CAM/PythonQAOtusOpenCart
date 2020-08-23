from selenium import webdriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class LoginPage(BasePage):

    """ OpenCart account login page """

    DIV_ACCOUNT_LOGIN = (By.ID, "account-login")
    INPUT_LOGIN_BUTTON = (By.CSS_SELECTOR, "input.btn.btn-primary")
    A_CONTINUE_BUTTON = (By.XPATH, "//div[@class='well']/a[contains(@class, 'btn')]")
    DIV_LIST_GROUP = (By.CLASS_NAME, "list-group")
    A_FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")

    def __init__(self, driver: webdriver, logging_enabled: bool, url: str = ""):
        self.driver: webdriver = driver
        self.url: str = url if url else "https://demo.opencart.com/index.php?route=account/login"
        super().__init__(
            driver=self.driver,
            url=self.url,
            logging_enabled=logging_enabled
        )
    #
#
