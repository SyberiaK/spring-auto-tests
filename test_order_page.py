import pytest
import os
import time
from .pages.auth_page import AuthPage
from .pages.order_page import OrderPage

main_link = 'http://u1609007.isp.regruhosting.ru/#'
login_link = 'http://u1609007.isp.regruhosting.ru/#/auth'
# page = OrderPage(browser, ...)


@pytest.fixture(scope='function', autouse=True)
def setup(browser):
    global page

    page = AuthPage(browser, login_link)
    page.open()

    page.should_be_auth_page()
    email = os.getenv('SPRING_ADMIN_MAIL')
    password = os.getenv('SPRING_ADMIN_PASSWORD')
    page.auth(email, password)

    page = OrderPage(browser, main_link)
    page.open()


@pytest.mark.begin
def test_begin(browser):
    page.should_be_create_order_button()


@pytest.mark.order
@pytest.mark.order_basis
class TestOrderBasis:
    def test_can_see_order_create_button(self, browser):
        page.should_be_create_order_button()

    def test_can_see_order_creation(self, browser):
        page.should_be_create_order_button()
        page.go_to_create_order()
        page.should_be_order_creation()

    def test_cant_see_order_creation(self, browser):
        page.should_be_create_order_button()
        page.should_not_be_order_creation()

    def test_can_cancel_order_creation(self, browser):
        page.go_to_create_order()
        page.go_to_cancel_order()
        page.cancel('leave')
        page.should_not_be_order_creation()

    def test_can_go_back_to_order_creation(self, browser):
        page.go_to_create_order()
        page.go_to_cancel_order()
        page.cancel('cancel')
        page.should_be_order_creation()


@pytest.mark.order
@pytest.mark.order_creation
class TestOrderCreation:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page.should_be_create_order_button()
        self.order_number = f'AUTOTEST_{int(time.time())}'
        page.create_order(self.order_number)

    def test_can_see_order_draft_after_creation(self, browser):
        page.should_be_order_draft()
        page.should_not_be_order_creation()

    def test_expected_order_info_equals_actual(self, browser):
        page.open()
        page.check_order_info(self.order_number)

    def test_expected_order_info_equals_actual_in_draft(self, browser):
        page.check_order_draft_info(self.order_number)

    def test_edit_and_save_see_summary(self, browser):
        order_number = f'EDITED_{self.order_number}'
        date = '30.03.2002'
        provider = '123123'

        page.edit_order_field('number', order_number)
        page.edit_order_field('date', date)
        page.edit_order_field('provider', provider)
        page.save_order()

        OrderPage(browser, main_link).open()
        page.check_order_info(order_number, date, provider)

    def test_edit_and_save_see_draft(self, browser):
        order_number = f'EDITED_{self.order_number}'
        date = '30.03.2002'
        shop = 'Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1'
        provider = '123123'

        page.edit_order_field('number', order_number)
        page.edit_order_field('date', date)
        page.edit_order_field('shop', shop)
        page.edit_order_field('provider', provider)
        page.save_order()

        same_page = OrderPage(browser, main_link)
        same_page.open()
        page.go_to_order()
        page.check_order_draft_info(order_number, date, shop, provider)

    def test_edit_and_not_save_see_summary(self, browser):
        order_number = f'EDITED_{self.order_number}'
        date = '30.03.2002'
        provider = '123123'

        page.edit_order_field('number', order_number)
        page.edit_order_field('date', date)
        page.edit_order_field('provider', provider)
        # page.save_order()    # не сохраняем!

        OrderPage(browser, main_link).open()
        page.check_order_info(self.order_number)    # поэтому сверяем со старыми данными (дефолтными)

    def test_edit_and_not_save_see_draft(self, browser):
        order_number = f'EDITED_{self.order_number}'
        date = '30.03.2002'
        shop = 'Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1 Shop 1'
        provider = '123123'

        page.edit_order_field('number', order_number)
        page.edit_order_field('date', date)
        page.edit_order_field('shop', shop)
        page.edit_order_field('provider', provider)
        # page.save_order()    # не сохраняем!

        OrderPage(browser, main_link).open()
        page.go_to_order()
        page.check_order_draft_info(self.order_number)    # поэтому сверяем со старыми данными (дефолтными)


@pytest.mark.element
@pytest.mark.element_basis
class TestElementBasis:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page.should_be_create_order_button()
        self.order_number = f'AUTOTEST_{int(time.time())}'
        page.create_order(self.order_number)

    def test_can_add_element(self, browser):
        page.should_be_order_draft()

    def test_can_see_element_creation(self, browser):
        page.should_be_order_draft()
        page.go_to_create_element()
        page.should_be_element_creation()

    def test_cant_see_element_creation(self, browser):
        page.should_be_order_draft()
        page.should_not_be_element_creation()

    def test_can_cancel_element_creation(self, browser):
        page.go_to_create_element()
        page.go_to_cancel_element()
        page.cancel('leave')
        page.should_not_be_element_creation()

    def test_can_go_back_to_order_creation(self, browser):
        page.go_to_create_element()
        page.go_to_cancel_element()
        page.cancel('cancel')
        page.should_be_element_creation()


@pytest.mark.element
@pytest.mark.element_creation
class TestElementCreation:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page.should_be_create_order_button()
        self.order_number = f'AUTOTEST_{int(time.time())}'
        page.create_order(self.order_number)
        page.should_be_order_draft()
        page.create_element()

    def test_can_see_order_draft_after_creation(self, browser):
        page.should_be_order_draft()
        page.should_not_be_element_creation()

    def test_expected_element_info_equals_actual(self, browser):
        page.check_element_info(self.order_number)

    def test_save_and_reload(self, browser):
        page.save_order()
        OrderPage(browser, main_link).open()
        page.go_to_order()
        page.should_be_any_element()

    def test_not_save_and_reload(self, browser):
        # page.save_order()  # не сохраняем!
        OrderPage(browser, main_link).open()
        page.go_to_order()
        page.should_not_be_any_element()  # поэтому элементов не должно быть

    def test_delete_save_and_reload(self, browser):
        page.go_to_delete_element()
        page.delete_element('delete')
        page.save_order()
        OrderPage(browser, main_link).open()
        page.go_to_order()
        page.should_not_be_any_element()

    def test_delete_save_and_reload(self, browser):
        page.go_to_delete_element()
        page.delete_element('delete')
        # page.save_order()  # не сохраняем!
        OrderPage(browser, main_link).open()
        page.go_to_order()
        page.should_not_be_any_element()  # поэтому элемент должен остаться

    def test_can_cancel_deletion(self, browser):
        page.go_to_delete_element()
        page.delete_element('cancel')
        page.should_be_any_element()

    def test_can_add_few_elements(self, browser):
        page.create_element()
        page.create_element()
        page.count_elements(3)

    def test_can_add_few_elements_and_save(self, browser):
        page.create_element()
        page.create_element()
        page.count_elements(3)
        page.save_order()
        OrderPage(browser, main_link).open()
        page.go_to_order()
        page.count_elements(3)

    def test_can_add_few_elements_and_not_save(self, browser):
        page.create_element()
        page.create_element()
        page.count_elements(3)
        # page.save_order()  # не сохраняем!
        OrderPage(browser, main_link).open()
        page.go_to_order()
        page.should_not_be_any_element()  # поэтому элементов не должно быть

    def test_can_add_few_elements_and_save_then_add_few_elements_and_save(self, browser):
        page.create_element()
        page.create_element()
        page.count_elements(3)
        page.save_order()
        page.create_element()
        page.create_element()
        page.create_element()
        page.count_elements(6)
        page.save_order()
        OrderPage(browser, main_link).open()
        page.go_to_order()
        page.count_elements(6)

    def test_can_add_few_elements_and_save_then_add_few_elements_and_not_save(self, browser):
        page.create_element()
        page.create_element()
        page.count_elements(3)
        page.save_order()
        page.create_element()
        page.create_element()
        page.create_element()
        page.count_elements(6)
        # page.save_order()  # не сохраняем!
        OrderPage(browser, main_link).open()
        page.go_to_order()
        page.count_elements(3)  # поэтому элементов должно быть 3
