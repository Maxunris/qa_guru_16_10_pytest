import pytest
from selene import browser
from selenium import webdriver

@pytest.fixture
def browser_size(request):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.base_url = 'https://github.com/'
    [width, height] = request.param
    browser.config.window_width = width
    browser.config.window_height = height
    yield
    browser.quit()

@pytest.mark.parametrize("browser_size", [(1920, 1080), (1600, 900)], indirect=True)
def test_desktop(browser_size):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()


@pytest.mark.parametrize("browser_size", [(800, 400), (896, 414)], indirect=True)
def test_mobile(browser_size):
    browser.open('')
    browser.element('.Button--link .Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()


