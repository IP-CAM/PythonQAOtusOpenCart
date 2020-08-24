import pytest
from selenium import webdriver

from pages.product_page import ProductPage


@pytest.fixture(scope="function")
def product_page(browser: webdriver, page_logging) -> ProductPage:
    product_page = ProductPage(driver=browser, logging_enabled=page_logging)
    product_page.open_page()
    return product_page
#
