from selenium import webdriver
from selenium.webdriver.common.by import By

from .base_page import BasePage


class CatalogPage(BasePage):

    """ OpenCart catalog page """

    DIV_PRODUCT_CATEGORY = (By.ID, "product-category")
    IMG_THUMBNAIL = (By.CSS_SELECTOR, ".img-thumbnail")
    LABEL_SORT_BY = (By.XPATH, "//div[contains(@class, 'form-group') and contains(@class, 'input-group')]/label[@for='input-sort']")
    UL_BREADCRUMB = (By.CLASS_NAME, "breadcrumb")
    A_PRODUCT_COMPARE = (By.PARTIAL_LINK_TEXT, "Product Compare")

    def __init__(self, driver: webdriver, logging_enabled: bool, url: str = ""):
        self.driver: webdriver = driver
        self.url: str = url if url else "https://demo.opencart.com/index.php?route=product/category&path=20"
        super().__init__(
            driver=self.driver,
            url=self.url,
            logging_enabled=logging_enabled
        )
    #
#
