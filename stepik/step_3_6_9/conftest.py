import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome',
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                    help="Select language")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser")
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        sel_lang = request.config.getoption('language')
        options = Options()
        options.add_experimental_option('prefs',{'intl.accept_languages': sel_lang})
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        sel_lang2 = request.config.getoption('language')
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", sel_lang2)
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError(" should be chrome or firefox")

    yield browser
    print("\nquit browser..")
    browser.quit()