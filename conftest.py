import pytest
from selenium import webdriver


@pytest.fixture(scope="module")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    capabilities = {
        "browserName": "chrome",
        "browserVersion": "91.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": False
        }
    }

    browser = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities,
        options=options)

    return browser
