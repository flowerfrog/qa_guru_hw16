"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
import pytest
from selene import browser
from pages.main_page import MainPage


@pytest.fixture
def desktop_setup():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()


@pytest.fixture
def mobile_setup():
    browser.config.window_width = 375
    browser.config.window_height = 667
    yield
    browser.quit()


def test_github_desktop(desktop_setup):
    main_page = MainPage()
    main_page.open()
    main_page.clicking_on_login_button_in_desktop()
    main_page.should_redirect_to_page_login()


def test_github_mobile(mobile_setup):
    main_page = MainPage()
    main_page.open()
    main_page.clicking_on_login_button_in_mobile()
    main_page.should_redirect_to_page_login()
