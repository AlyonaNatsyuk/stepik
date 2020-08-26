import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestLanguage:

    def test_find_button(self, browser):
        browser.get(link)
        time.sleep(5)
        button = browser.find_element_by_css_selector("button[class='btn btn-lg btn-primary btn-add-to-basket']")
        assert button, f"There is no button, sorry"