from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    digit1 = browser.find_element_by_css_selector("[id='num1']")
    x1 = digit1.text
    digit2 = browser.find_element_by_css_selector("[id='num2']")
    x2 = digit2.text
    summary = str(int(x1) + int(x2))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(summary)
    button = browser.find_element_by_class_name("btn-default")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()