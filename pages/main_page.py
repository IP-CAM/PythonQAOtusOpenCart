from selenium import webdriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):

    """ OpenCart main page """

    DIV_ID_SLIDESHOW = (By.ID, "slideshow0")
    DIV_CSS_SLIDESHOW = (By.CSS_SELECTOR, "#slideshow0")
    DIV_XPATH_SLIDESHOW = (By.XPATH, "//div[@id='slideshow0']")
    DIV_CLASS_SLIDESHOW = (By.CLASS_NAME, "swiper-container.swiper-container-horizontal")
    A_YOUR_STORE = (By.LINK_TEXT, "Your Store")

    BUTTON_CURRENCY = (By.XPATH, "//form[@id='form-currency']/div/button")
    BUTTON_EUR = (By.XPATH, "//form[@id='form-currency']/div/ul/li/button[@name='EUR']")
    BUTTON_GBP = (By.XPATH, "//form[@id='form-currency']/div/ul/li/button[@name='GBP']")
    BUTTON_USD = (By.XPATH, "//form[@id='form-currency']/div/ul/li/button[@name='USD']")
    STRONG_CURRENT_CURRENCY = (By.XPATH, "//form[@id='form-currency']//strong")

    A_DROPDOWN = (By.XPATH, "//div[@id='top-links']/ul/li[@class='dropdown']/a")
    A_DROPDOWN_OPEN = (By.XPATH, "//div[@id='top-links']/ul/li[@class='dropdown open']/a")
    A_REGISTER = (By.XPATH, "(//div[@id='top-links']/ul/li[@class='dropdown open']/ul/li/a)[1]")
    A_LOGIN = (By.XPATH, "(//div[@id='top-links']/ul/li[@class='dropdown open']/ul/li/a)[2]")

    BUTTON_ADD_TO_CART = (By.XPATH, "(//div[@id='content']//div[@class='row']/div//div[@class='button-group'])[1]/button[1]")
    A_PRODUCT_NAME = (By.XPATH, "(//div[@id='content']//div[@class='row']/div//div[@class='caption'])[1]/h4/a")
    BUTTON_VIEW_CART = (By.XPATH, "//div[@id='cart']/button")
    P_CART_IS_EMPTY = (By.XPATH, "//div[@id='cart']/ul/li/p")
    A_PRODUCT_ADDED = (By.XPATH, "(//div[@class='alert alert-success alert-dismissible']/a)[1]")

    def __init__(self, driver: webdriver, logging_enabled: bool, url: str = ""):
        self.driver: webdriver = driver
        self.url: str = url if url else "https://demo.opencart.com"
        super().__init__(
            driver=self.driver,
            url=self.url,
            logging_enabled=logging_enabled
        )
        self.product_name: str = ""
    #

    def get_current_currency(self) -> str:
        """ Get currently selected currency for prices """
        return self.find_element(locator=self.STRONG_CURRENT_CURRENCY).text
    #

    def change_currency(self, new_currency: str):
        """ Change currency in top-left corner of main page """
        self.find_element(locator=self.BUTTON_CURRENCY).click()
        if new_currency == "EUR":
            self.find_element(locator=self.BUTTON_EUR).click()
        if new_currency == "GBP":
            self.find_element(locator=self.BUTTON_GBP).click()
        if new_currency == "USD":
            self.find_element(locator=self.BUTTON_USD).click()
    #

    def open_my_account_dropdown(self):
        """ Open My Account dropdown list to check Register and Login links """
        self.find_element(locator=self.A_DROPDOWN).click()
    #

    def is_cart_empty(self) -> bool:
        """ Check if cart is empty at the moment"""
        self.find_element(locator=self.BUTTON_VIEW_CART).click()
        if self.find_element(locator=self.P_CART_IS_EMPTY):
            return True
        return False
    #

    def add_to_cart(self):
        """ Add item from main page to cart"""
        self.find_element(locator=self.BUTTON_ADD_TO_CART).click()
        self.product_name = self.find_element(locator=self.A_PRODUCT_NAME).text
    #

    def check_product_added_to_cart(self) -> bool:
        """ Check that after clicking "Add to cart" button product was added to cart"""
        assert self.find_element(locator=self.A_PRODUCT_ADDED).text == self.product_name
    #
#

