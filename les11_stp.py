from selenium import webdriver
import time
import math
from numpy import log as ln

link = ' http://suninjuly.github.io/get_attribute.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)

    images = browser.find_element_by_id('treasure')
    x = images.get_attribute('valuex')


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    input = browser.find_element_by_tag_name('input')
    input.send_keys(calc(x))

    check = browser.find_element_by_id('robotCheckbox')
    check.click()

    check2 = browser.find_element_by_id('robotsRule')
    check2.click()

    button =browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(30)