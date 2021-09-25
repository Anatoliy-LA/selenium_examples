from pages.base import BasePage
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class AliPhonesPage(BasePage):
    advertisment_xpath = "//body/div[@id='__aer_root__']/div/div/div[2]/div[1]/button[1]"
    phones_xpath = '//*[@id="__aer_root__"]/div/div[5]/div/ul/li[1]/div[1]/a'
    advertisment_2_xpath = "//a[@aria-label='关闭']"
    min_value_xpath = "//input[@placeholder='мин']"
    max_value_xpath = "//input[@placeholder='макс']"
    ok_xpath = "//a[@class='ui-button narrow-go']"
    phones_list_xpath = "//div[@class='list-wrap product-list']//li"
    free_xpath = '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[3]/span[2]/label/span[1]/input'

    def __init__(self):  # , browser
        BasePage.__init__(self)
        # self.browser = browser
        print("===PhonesPage===")

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
        # self.browser = webdriver.Remote(
        #     command_executor="http://localhost:4444/wd/hub",
        #     desired_capabilities=capabilities,
        #     options=options)
        self.browser = webdriver.Firefox()

    def test_page(self):
        url = "http://aliexpress.ru/"
        print("===1===")
        self.browser.get(url)    # visit site
        print("===2===")

        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located((By.XPATH, self.advertisment_xpath))).click()    # wait and click advertisment
        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located((By.XPATH, self.phones_xpath))).click()
        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located((By.XPATH, self.advertisment_2_xpath))).click()    # wait and click advertisment page 2

        free = self.browser.find_element_by_xpath(self.free_xpath)
        free.click()
        value = self.browser.find_element_by_xpath(self.min_value_xpath)  # input min value
        value.send_keys("5000")
        value2 = self.browser.find_element_by_xpath(self.max_value_xpath)  # input max value
        value2.send_keys("15000")
        ok = self.browser.find_element_by_xpath(self.ok_xpath)  # input ok
        ok.click()

        WebDriverWait(self.browser, 180).until(EC.presence_of_element_located((By.XPATH, self.free_xpath))).click()

        # count of number phones
        phone_count = len(self.browser.find_elements_by_xpath(self.phones_list_xpath))
        print(phone_count)

        # test
        assert phone_count >= 50, "Phone number is less then 50"

        # sleep and take screenshot
        print("===3===")
        self.browser.save_screenshot("screenshots/screen_ali.png")
        print("===4===")

        # quit
        print("THE END!")
        self.browser.quit()
