"""
Параметризуйте фикстуру несколькими вариантами размеров окна.
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser
from pages.main_page import MainPage


@pytest.fixture(params=[(1920, 1080, 'desktop'), (375, 667, 'mobile')])
def browser_setup(request):
    if request.param[2] == 'desktop':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]

    if request.param[2] == 'mobile':
        browser.config.window_width = request.param[0]
        browser.config.window_height = request.param[1]
        return request.param[2]


def test_github_desktop(browser_setup):
    if browser_setup == 'mobile':
        pytest.skip('this test is not for mobile size browsers')
    main_page = MainPage()
    main_page.open()
    main_page.clicking_on_login_button_in_desktop()
    main_page.should_redirect_to_page_login()


def test_github_mobile(browser_setup):
    if browser_setup == 'desktop':
        pytest.skip('this test is not for desktop size browsers')
    main_page = MainPage()
    main_page.open()
    main_page.clicking_on_login_button_in_mobile()
    main_page.should_redirect_to_page_login()
