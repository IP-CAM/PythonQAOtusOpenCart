import json
import logging

import allure
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from configuration import PAGE_TIMEOUT


class BasePage:

    """
    Base class implementing Page Object Model pattern
    """

    def __init__(self,
                 driver: webdriver,
                 url: str = "",
                 logging_enabled: bool = False,
                 timeout: int = PAGE_TIMEOUT):
        self.driver: webdriver = driver
        self.url: str = url if url else "https://demo.opencart.com"
        self.timeout: int = timeout
        self.logging_enabled: bool = logging_enabled

        if self.logging_enabled:
            self.handler = logging.FileHandler(filename=f"{type(self).__name__}.log")
            self.formatter = logging.Formatter(fmt="%(asctime)s\t%(name)s\t%(levelname)s\t%(message)s")
            self.handler.setFormatter(fmt=self.formatter)

            self.logger = logging.getLogger(name=type(self).__name__)
            self.logger.setLevel(level=logging.INFO)
            self.logger.addHandler(hdlr=self.handler)
    #

    def find_element(self, locator):
        """
        Basic method that searches for web element of HTML page by given locator
        """
        try:
            if self.logging_enabled:
                self.logger.info(f"Finding element by locator {locator}")
            element = WebDriverWait(driver=self.driver, timeout=self.timeout).until(
                method=EC.visibility_of_element_located(locator),
                message=f"Can't find element by locator {locator}"
            )
            if element:
                if self.logging_enabled:
                    self.logger.info(f"Found element {element} by locator {locator}")
                return element
        except TimeoutException:
            # Allure: attach desired capabilities
            allure.attach(
                body=json.dumps(self.driver.capabilities, indent=4),
                name="Capabilities",
                attachment_type=allure.attachment_type.JSON
            )
            # Allure: attach Chrome logs
            if self.driver.capabilities.get("browserName") == "chrome":
                allure.attach(
                    body=json.dumps(self.driver.get_log("browser"), indent=4),
                    name="Browser logs",
                    attachment_type=allure.attachment_type.JSON
                )
            # Allure: attach browser screenshot
            allure.attach(
                body=self.driver.get_screenshot_as_png(),
                name="Screenshot",
                attachment_type=allure.attachment_type.PNG
            )
            if self.logging_enabled:
                self.logger.error(f"Failed to find element by locator {locator}")
                self.logger.error(f'Caught {TimeoutException.__name__}:\n{TimeoutException}')
                self.logger.error(f'Saving screenshot to {TimeoutException.__name__}.png')
                self.driver.save_screenshot(filename='TimeoutException.png')
    #

    def find_elements(self, locator):
        return WebDriverWait(driver=self.driver, timeout=self.timeout).until(
            method=EC.visibility_of_all_elements_located(locator),
            message=f"Can't find elements by locator {locator}"
        )
    #

    def open_page(self):
        """
        Open page in browser window
        """
        return self.driver.get(url=self.url)
    #
#
