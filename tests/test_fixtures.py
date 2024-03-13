
from selene import browser

def test_desktop(desktop_browser_size):
    browser.open('')
    browser.element('.HeaderMenu-link--sign-in').click()

def test_mobile(mobile_browser_size):
    browser.open('')
    browser.element('.Button--link .Button-content').click()
    browser.element('.HeaderMenu-link--sign-in').click()
