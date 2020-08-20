from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    image = browser.find_element_by_css_selector("[id ='treasure'][valuex]")
    x_element = image.get_attribute("valuex")
    y = calc(x_element)
    input1 = browser.find_element_by_css_selector("[id='answer']")
    input1.send_keys(y)
    checkbox = browser.find_element_by_css_selector("[id='robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[id='robotsRule']")
    radiobutton.click()
    button = browser.find_element_by_class_name("btn-default")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()