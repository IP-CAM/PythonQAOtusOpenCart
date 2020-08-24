import pytest
from _pytest.config.argparsing import Parser
from _pytest.fixtures import FixtureRequest
from selenium import webdriver

pytest_plugins = [
    "fixtures.fixtures_admin_login_page",
    "fixtures.fixtures_administration_page",
    "fixtures.fixtures_catalog_page",
    "fixtures.fixtures_main_page",
    "fixtures.fixtures_product_page",
    "fixtures.fixtures_user_login_page"
]


@pytest.fixture(scope="function")
def page_logging(request) -> bool:
    """
    Parse "--page_logging" tag from command line to log
    actions in base page class and its descendants
    """
    if request.config.getoption(name="--page_logging"):
        return True
    else:
        return False
#


@pytest.fixture(scope="function")
def browser(request: FixtureRequest) -> webdriver:
    """
    Launch browser in Selenoid
    """
    browser_name = request.config.getoption(name="--browser_name")
    browser_version = request.config.getoption(name="--browser_version")
    selenoid_hostname = request.config.getoption(name="--selenoid_hostname")
    executor_url = f"http://{selenoid_hostname}:4444/wd/hub"
    capabilities = {
        "browserName": browser_name,
        "name": request.node.name,  # test name
        "version": browser_version,
        "enableVNC": True,
        "enableVideo": True
    }
    driver = webdriver.Remote(
        command_executor=executor_url,
        desired_capabilities=capabilities
    )
    request.addfinalizer(driver.quit)
    driver.maximize_window()
    return driver
#


@pytest.fixture(scope="function")
def opencart_url(request: FixtureRequest) -> str:
    """
    URL of OpenCart page (absolute or relative to https://localhost)
    """
    url = str(request.config.getoption("--opencart_url"))
    if url.startswith("https://"):
        return url
    elif url.startswith("/"):
        return f"https://localhost{url}"
    else:
        raise ValueError(f"Incorrect url: {url}")
#


# Init hook
def pytest_addoption(parser: Parser):

    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        choices=["firefox", "chrome", "opera"],
        help="Browser name used to invoke corresponding web driver in Selenoid (defaults to chrome)"
    )
    parser.addoption(
        "--browser_version",
        action="store",
        default="",
        help="Particular browser version used to invoke corresponding web driver in Selenoid (defaults to latest)"
    )
    parser.addoption(
        "--selenoid_hostname",
        action="store",
        default="localhost",
        help="Selenoid host name (used as part of web driver command executor)"
    )
    parser.addoption(
        "--opencart_url",
        action="store",
        default="https://demo.opencart.com",
        help="URL of OpenCart page (defaults to main page https://demo.opencart.com)"
    )
    parser.addoption(
        "--page_logging",
        action="store_true",
        help="Log actions on pages"
    )
#
