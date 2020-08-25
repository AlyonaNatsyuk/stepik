import time
import math

import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('site', ["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, site):
    link = f"{site}"
    browser.get(link)
    time.sleep(10)
    input1 = browser.find_element_by_css_selector("textarea[placeholder='Напишите ваш ответ здесь...']")
    input1.send_keys(str(math.log(int(time.time()))))
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
    time.sleep(15)
    input2 = browser.find_element_by_css_selector("pre[class='smart-hints__hint']")
    x = input2.text
    assert "Correct!" == x, f"error in ask: {x}"