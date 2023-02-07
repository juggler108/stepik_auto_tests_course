from selenium import webdriver
from time import sleep
from math import log, sin

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"


def calc(x):
    return str(log(abs(12*sin(int(x)))))


try:
    browser.get(link)

    sleep(1)
    browser.find_element(by="class name", value="btn").click()

    sleep(1)
    browser.switch_to.alert.accept()

    x = browser.find_element(by="id", value="input_value").text
    browser.find_element(by="id", value="answer").send_keys(calc(x))

    sleep(1)
    browser.find_element(by="class name", value="btn").click()

    print(browser.switch_to.alert.text)

finally:
    browser.quit()
