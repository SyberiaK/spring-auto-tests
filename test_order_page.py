import pytest
import os
import time
from pages.auth_page import AuthPage
from pages.order_page import OrderPage

page = ...


@pytest.fixture(scope='function', autouse=True)
def setup(browser):
    global page

    login_link = 'http://u1609007.isp.regruhosting.ru/#/auth'
    page = AuthPage(browser, login_link)
    page.open()
    page.should_be_auth_page()
    email = os.getenv('SPRING_ADMIN_MAIL')
    password = os.getenv('SPRING_ADMIN_PASSWORD')
    page.auth(email, password)
    page.should_not_be_auth_page()
    link = 'http://u1609007.isp.regruhosting.ru/#'
    page = OrderPage(browser, link)
    page.open()


def test_can_see_order_create_button(browser):
    page.should_be_create_order_button()


def test_can_see_order_creation(browser):
    page.should_be_create_order_button()
    page.click_create_order()
    page.should_be_order_creation()


def test_cant_see_order_creation(browser):
    page.should_be_create_order_button()
    page.should_not_be_order_creation()


class TestCreationOrder:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page.should_be_create_order_button()
        self.order_number = f'AUTOTEST_{int(time.time())}'
        page.create_order(self.order_number)

    def test_can_create_order(self, browser):
        pass

    def test_can_see_order_draft_after_creation(self, browser):
        page.should_be_order_draft()

    def test_expected_order_info_equals_actual(self, browser):
        page.open()
        page.check_order_info(self.order_number)

    def test_expected_order_info_equals_actual_in_draft(self, browser):
        page.check_order_draft_info(self.order_number)

    def test_edit_and_save_see_summary(self, browser):
        order_number = f'EDITED_{self.order_number}'
        page.edit_order_field('number', order_number)
        date = '30.03.2002'
        page.edit_order_field('date', date)
        provider = '123123'
        page.edit_order_field('provider', provider)
        page.save_order()
        link = 'http://u1609007.isp.regruhosting.ru/#'
        same_page = OrderPage(browser, link)
        same_page.open()
        same_page.check_order_info(order_number, date, provider)

    def test_edit_and_save_see_draft(self, browser):
        order_number = f'EDITED_{self.order_number}'
        page.edit_order_field('number', order_number)
        date = '30.03.2002'
        page.edit_order_field('date', date)
        shop = 'Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1'
        page.edit_order_field('shop', shop)
        provider = '123123'
        page.edit_order_field('provider', provider)
        page.save_order()
        link = 'http://u1609007.isp.regruhosting.ru/#'
        same_page = OrderPage(browser, link)
        same_page.open()
        same_page.go_to_order()
        same_page.check_order_draft_info(order_number, date, shop, provider)

    def test_edit_see_summary(self, browser):
        order_number = f'EDITED_{self.order_number}'
        page.edit_order_field('number', order_number)
        date = '30.03.2002'
        page.edit_order_field('date', date)
        provider = '123123'
        page.edit_order_field('provider', provider)
        # page.save_order()    # не сохраняем!
        link = 'http://u1609007.isp.regruhosting.ru/#'
        same_page = OrderPage(browser, link)
        same_page.open()
        same_page.check_order_info(self.order_number)    # поэтому сверяем со старыми данными (дефолтными)

    def test_edit_see_summary(self, browser):
        order_number = f'EDITED_{self.order_number}'
        page.edit_order_field('number', order_number)
        date = '30.03.2002'
        page.edit_order_field('date', date)
        shop = 'Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1'
        page.edit_order_field('shop', shop)
        provider = '123123'
        page.edit_order_field('provider', provider)
        # page.save_order()    # не сохраняем!
        link = 'http://u1609007.isp.regruhosting.ru/#'
        same_page = OrderPage(browser, link)
        same_page.open()
        same_page.go_to_order()
        same_page.check_order_draft_info(self.order_number)    # поэтому сверяем со старыми данными (дефолтными)
