from selenium import webdriver
import time
import math

try:
    link = "https://stepik.org/lesson/236905/step/1"
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(10)
    # Ваш код, который заполняет обязательные поля

    input1 = browser.find_element_by_css_selector("textarea[placeholder='Напишите ваш ответ здесь...']")
    input1.send_keys(str(math.log(int(time.time()))))

    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(10)
    input2 = browser.find_element_by_css_selector("pre[class='smart-hints__hint']")
    x = input2.text
    assert "Correct!" == x, "error in ask"

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
