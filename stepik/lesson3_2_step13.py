import unittest
from selenium import webdriver
import time

class LessonUnit(unittest.TestCase):
    def test_site1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector("input[placeholder*='Input your first name']")
        first_name.send_keys("Alena")
        last_name = browser.find_element_by_css_selector("input[placeholder*='Input your last name']")
        last_name.send_keys("Natsyuk")
        email = browser.find_element_by_css_selector("input[placeholder*='Input your email']")
        email.send_keys("alena@gmail.com")
        button = browser.find_element_by_class_name("btn-default")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text, True)

    def test_site2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        first_name = browser.find_element_by_css_selector("input[placeholder*='Input your first name']")
        first_name.send_keys("Alena")
        last_name = browser.find_element_by_css_selector("input[placeholder*='Input your last name']")
        last_name.send_keys("Natsyuk")
        email = browser.find_element_by_css_selector("input[placeholder*='Input your email']")
        email.send_keys("alena@gmail.com")
        button = browser.find_element_by_class_name("btn-default")
        button.click()
        time.sleep(1)
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!" == welcome_text, True)


if __name__ == "__main__":
    unittest.main()
