from pages.base import BasePage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GithubMain(BasePage):
    xpath_201_plus = "//div[@class='col-sm-4 col-md-3 d-none d-md-block']//h2[1]"

    def __init__(self):  # , browser
        BasePage.__init__(self)
        # self.browser = browser
        print("===GithubMain===")

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

        # init browser
        self.browser = webdriver.Remote(
            command_executor="http://localhost:4444/wd/hub",
            desired_capabilities=capabilities,
            options=options)

    def test_page(self):
        url = "https://github.com/"
        print("===1===")
        self.browser.get(url)    # visit site
        print("===2===")

        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located((By.XPATH, self.xpath_201_plus))).click()    # wait and click advertisment

        # # test
        value = self.browser.find_element_by_xpath(self.xpath_201_plus)
        assert value.text == "200+ million"

        #  sleep and take screenshot
        print("===3===")
        self.browser.save_screenshot("screenshots/screen_github.png")
        print("===4===")

        # quit
        print("THE END!")
        self.browser.quit()
