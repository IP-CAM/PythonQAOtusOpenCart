import pytest
from selenium import webdriver

from pages.catalog_page import CatalogPage


@pytest.fixture(scope="function")
def catalog_page(browser: webdriver, page_logging) -> CatalogPage:
    catalog_page = CatalogPage(driver=browser, logging_enabled=page_logging)
    catalog_page.open_page()
    return catalog_page
#
