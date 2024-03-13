import pytest
from selene import browser
from selenium import webdriver


def test_desktop(desktop_browser_size):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.base_url = 'https://github.com/'
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()


def test_mobile(mobile_browser_size):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.base_url = 'https://github.com/'
    browser.open('')
    browser.element('.Button--link .Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.fixture(params=[(1920, 1080), (1600, 900)])
def desktop_browser_size(request):
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()


@pytest.fixture(params=[(800, 400), (896, 414)])
def mobile_browser_size(request):
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()
