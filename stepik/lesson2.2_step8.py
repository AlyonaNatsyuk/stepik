import os
from selenium import webdriver
import time


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name = browser.find_element_by_css_selector("[name='firstname']")
    name.send_keys("Alyona")
    lastname = browser.find_element_by_css_selector("[name='lastname']")
    lastname.send_keys("Natsyuk")
    email = browser.find_element_by_css_selector("[name='email']")
    email.send_keys("test@test.com")
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    element = browser.find_element_by_css_selector("[name='file']")
    element.send_keys(file_path)
    button = browser.find_element_by_class_name("btn-primary")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()