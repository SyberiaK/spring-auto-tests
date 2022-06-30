from .base_page import BasePage
from .locators import AuthPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class AuthPage(BasePage):
    def should_be_auth_page(self):
        assert 'auth' in self.browser.current_url, 'This page is not a auth page'
        assert self.is_element_present(*AuthPageLocators.EMAIL_INPUT), 'Email input is not presented'
        assert self.is_element_present(*AuthPageLocators.PASSWORD_INPUT), 'Password input is not presented'

    def auth(self, email, password):
        self.browser.find_element(*AuthPageLocators.EMAIL_INPUT).send_keys(email)
        self.browser.find_element(*AuthPageLocators.PASSWORD_INPUT).send_keys(password)

        # lh, lw = AuthPageLocators.LOGIN_BTN
        # assert self.is_element_present(*AuthPageLocators.LOGIN_BTN), 'Login button is not presented'
        # WebDriverWait(self.browser, 4, 1, AssertionError('Login button is not clickable')).\
        #     until(ec.element_to_be_clickable((lh, lw)))

        self.browser.find_element(*AuthPageLocators.LOGIN_BTN).click()
        # self.browser.find_element(*AuthPageLocators.LOGIN_BTN).click()
