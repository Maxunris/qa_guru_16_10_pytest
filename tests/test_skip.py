import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture(params=[(1920, 1080), (1600, 900), (800, 400), (896, 414)])
def browser_size(request):
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    return width, height


def test_desktop(browser_size):
    width, height = browser_size
    if width >= 1600:
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        browser.config.base_url = 'https://github.com/'
        browser.open('')

        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip("Пропускаем десктоп")


def test_mobile(browser_size):
    width, height = browser_size
    if width < 1600:
        driver_options = webdriver.ChromeOptions()
        driver_options.page_load_strategy = 'eager'
        browser.config.base_url = 'https://github.com/'
        browser.open('')
        browser.element('.Button--link .Button-content').click()
        browser.element('.HeaderMenu-link--sign-in').click()
    else:
        pytest.skip("Пропускаем мобильные.")
