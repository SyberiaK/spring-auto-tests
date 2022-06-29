import pytest
import os
from .pages.auth_page import AuthPage
from .pages.order_page import OrderPage


@pytest.fixture(scope='function', autouse=True)
def setup(browser):
    login_link = 'http://u1609007.isp.regruhosting.ru/#/auth'
    page = AuthPage(browser, login_link)
    page.open()
    page.should_be_auth_page()
    email = os.getenv('SPRING_ADMIN_MAIL')
    password = os.getenv('SPRING_ADMIN_PASSWORD')
    page.auth(email, password)
    page.should_not_be_auth_page()


def test_can_add_order(browser):
    link = 'http://u1609007.isp.regruhosting.ru/#'
    page = OrderPage(browser, link)