from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
# from time import sleep


# advertisment_xpath = "//body/div[@id='__aer_root__']/div/div/div[2]/div[1]/button[1]"
advertisment2 = "//a[@aria-label='关闭']"
phone_url = "https://aliexpress.ru/category/202000054/cellphones-telecommunications.html?spm=a2g0o.home.103.1.75df4aa6dC6OoQ"
banned_sign_xpath = "/html/body/div/div[2]/div/div[1]/div[2]/div"
phones_list_xpath = "//div[@class='list-wrap product-list']//li"
free_xpath = "//input[@aria-checked='true']"

min_xpath = "//input[@placeholder='мин']"
max_xpath = "//input[@placeholder='макс']"
ok_xpath = "//a[@class='ui-button narrow-go']"

# wait and click advertisment
# WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, advertisment_xpath))).click()

browser = webdriver.Chrome()    # launch browser
browser.get(phone_url)    # visit site

# ta = browser.find_element_by_xpath("//a[contains(text(),'Телефоны и аксессуары')]")
# ta.click()

if browser.find_element_by_xpath(banned_sign_xpath):
    print("we_are_banned!")
else:
    # wait and click advertisment page 2
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, advertisment2))).click()

    free = browser.find_element_by_xpath(free_xpath)
    free.click()

    value = browser.find_element_by_xpath(min_xpath)
    value.send_keys("5000")
    value2 = browser.find_element_by_xpath(max_xpath)
    value2.send_keys("15000")
    ok = browser.find_element_by_xpath(ok_xpath)
    ok.click()

    # count of number phones
    print(len(browser.find_elements_by_xpath(phones_list_xpath)))

# take screenshot
# browser.save_screenshot("screen_ban_ali.png")

# quit
browser.quit()
