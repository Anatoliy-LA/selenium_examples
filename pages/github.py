from pages.base import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class GithubMain(BasePage):
    xpath_201_plus = "//div[@class='col-sm-4 col-md-3 d-none d-md-block']//h2[1]"

    def __init__(self):
        BasePage.__init__(self)
        print("===GithubMain===")

    def test_main_page(self, browser):
        url = "https://github.com/"
        print("===1===")
        browser.get(url)    # visit site
        print("===2===")

        WebDriverWait(browser, 180).until(EC.presence_of_element_located((By.XPATH, self.xpath_201_plus))).click()    # wait and click advertisment

        # # test
        value = browser.find_element_by_xpath(self.xpath_201_plus)
        assert value.text == "200+ million"

        #  sleep and take screenshot
        print("===3===")
        browser.save_screenshot("screenshots/screen_github.png")
        print("===4===")

        # quit
        print("THE END!")
        browser.quit()
