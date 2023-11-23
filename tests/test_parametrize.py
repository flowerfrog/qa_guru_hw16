"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser
from pages.main_page import MainPage


@pytest.fixture(params=['desktop', 'mobile'])
def browser_setup(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080

    if request.param == 'mobile':
        browser.config.window_width = 375
        browser.config.window_height = 667
    yield
    browser.quit()


@pytest.mark.parametrize("browser_setup", ['desktop'], indirect=True)
def test_github_desktop(browser_setup):
    main_page = MainPage()
    main_page.open()
    main_page.clicking_on_login_button_in_desktop()
    main_page.should_redirect_to_page_login()


@pytest.mark.parametrize("browser_setup", ['mobile'], indirect=True)
def test_github_mobile(browser_setup):
    main_page = MainPage()
    main_page.open()
    main_page.clicking_on_login_button_in_mobile()
    main_page.should_redirect_to_page_login()
