# from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

url = "https://aliexpress.ru"

advertisment_xpath = "//body/div[@id='__aer_root__']/div/div/div[2]/div[1]/button[1]"
phones_xpath = '//*[@id="__aer_root__"]/div/div[5]/div/ul/li[1]/div[1]/a'
advertisment_2_xpath = "//a[@aria-label='关闭']"
min_value_xpath = "//input[@placeholder='мин']"
max_value_xpath = "//input[@placeholder='макс']"
ok_xpath = "//a[@class='ui-button narrow-go']"
phones_list_xpath = "//div[@class='list-wrap product-list']//li"
free_xpath = '//*[@id="root"]/div/div/div[2]/div[2]/div/div[1]/div[2]/div[1]/span[3]/span[2]/label/span[1]/input'


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
browser = webdriver.Remote(
    command_executor="http://localhost:4444/wd/hub",
    desired_capabilities=capabilities,
    options=options)
browser.get(url)    # visit site

WebDriverWait(browser, 180).until(EC.presence_of_element_located((By.XPATH, advertisment_xpath))).click()    # wait and click advertisment
WebDriverWait(browser, 180).until(EC.presence_of_element_located((By.XPATH, phones_xpath))).click()
WebDriverWait(browser, 180).until(EC.presence_of_element_located((By.XPATH, advertisment_2_xpath))).click()    # wait and click advertisment page 2

# free = browser.find_element_by_xpath(free_xpath)
# free.click()
value = browser.find_element_by_xpath(min_value_xpath)  # input min value
value.send_keys("5000")
value2 = browser.find_element_by_xpath(max_value_xpath)  # input max value
value2.send_keys("15000")
ok = browser.find_element_by_xpath(ok_xpath)  # input ok
ok.click()

WebDriverWait(browser, 180).until(EC.presence_of_element_located((By.XPATH, free_xpath))).click()

# count of number phones
phone_count = len(browser.find_elements_by_xpath(phones_list_xpath))
print(phone_count)

# for example
assert 2 + 2 == 4, "2+2 not equal 4"

# test
assert phone_count >= 50, "Phone number is less then 50"

#  sleep and take screenshot
browser.save_screenshot("screeenshots/screen1.png")

# quit
# print("THE END!")
browser.quit()
