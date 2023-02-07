from selenium import webdriver
import time
import math


browser = webdriver.Chrome()

# js = '''document.title='Test of JS';
#
# alert("JS in Selenium");
#
# console.log('hey there');
#
# '''
#
# browser.execute_script(js)
# time.sleep(10)


# link = "https://SunInJuly.github.io/execute_script.html"
# browser.get(link)
# button = browser.find_element(by="tag name", value="button")
# button.click()


# browser.get("https://suninjuly.github.io/execute_script.html")
# button = browser.find_element(by="tag name", value="button")
# time.sleep(2)
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
# button.click()
# time.sleep(5)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)

    x = browser.find_element(by="id", value="input_value").text
    answer = calc(x)

    browser.find_element(by="id", value="answer").send_keys(answer)

    button = browser.find_element(by="class name", value="btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(by="css selector", value="label[for='robotCheckbox']").click()
    browser.find_element(by="css selector", value="label[for='robotsRule']").click()
    button.click()

finally:
    time.sleep(5)
    browser.quit()
