from .base_page import BasePage
from .locators import AuthPageLocators


class AuthPage(BasePage):
    def should_be_auth_page(self):
        assert 'auth' in self.browser.current_url, 'This page is not a auth page'
        assert self.is_element_present(*AuthPageLocators.EMAIL_INPUT), "Email input is not presented"
        assert self.is_element_present(*AuthPageLocators.PASSWORD_INPUT), "Password input is not presented"
        assert self.is_element_present(*AuthPageLocators.LOGIN_SUBMIT), "Login button is not presented"

    def should_not_be_auth_page(self):
        assert 'auth' not in self.browser.current_url, 'This page is a auth page, but it shouldn\'t be'

    def auth(self, email, password):
        self.browser.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)
        self.browser.find_element(*AuthPageLocators.LOGIN_SUBMIT).click()