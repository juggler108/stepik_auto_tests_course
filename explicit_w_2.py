from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
browser.implicitly_wait(2)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    need_price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    if need_price:
        browser.find_element(by="id", value="book").click()

    num = calc(int(browser.find_element(by="id", value="input_value").text))
    browser.find_element(by="id", value="answer").send_keys(str(num))
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "solve"))
    )
    button.click()

    print(browser.switch_to.alert.text)

finally:
    browser.quit()



