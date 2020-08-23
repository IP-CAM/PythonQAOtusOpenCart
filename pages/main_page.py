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

    def __init__(self, driver: webdriver, logging_enabled: bool, url: str = ""):
        self.driver: webdriver = driver
        self.url: str = url if url else "https://demo.opencart.com"
        super().__init__(
            driver=self.driver,
            url=self.url,
            logging_enabled=logging_enabled
        )
    #
#
