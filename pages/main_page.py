from selene import browser, have


class MainPage:
    def open(self):
        browser.open('https://github.com/')
        return self

    def clicking_on_login_button_in_desktop(self):
        browser.element('a[href="/login"]').click()
        return self

    def clicking_on_login_button_in_mobile(self):
        browser.element('.Button--link').click()
        browser.element('a[href="/login"]').click()
        return self

    def should_redirect_to_page_login(self):
        browser.element('.auth-form-header').should(have.text('Sign in to GitHub'))
        return self
