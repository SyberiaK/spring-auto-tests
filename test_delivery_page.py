import pytest
import os
import time
from .pages.auth_page import AuthPage
from .pages.delivery_page import DeliveryPage

delivery_link = "http://u1609007.isp.regruhosting.ru/#/delivery"


@pytest.fixture(scope='function', autouse=True)
def setup(browser):
    global page

    page = AuthPage(browser, delivery_link)
    page.open()
    page.should_be_auth_page()
    email = os.getenv('SPRING_ADMIN_MAIL')
    password = os.getenv('SPRING_ADMIN_PASSWORD')
    page.auth(email, password)

    page = DeliveryPage(browser, delivery_link)
    time.sleep(1)
    page.open()


@pytest.mark.delivery
@pytest.mark.delivery_basis
class TestDeliveryBasis:
    def test_can_see_delivery_create_button(self, browser):
        page.should_be_create_delivery_button()

    def test_can_see_delivery_creation(self, browser):
        page.should_be_create_delivery_button()
        page.go_to_create_delivery()
        page.should_be_delivery_creation()

    def test_cant_see_delivery_creation(self, browser):
        page.should_be_create_delivery_button()
        page.browser.implicitly_wait(0)
        page.should_not_be_delivery_creation("pres")

    def test_can_cancel_delivery_creation(self, browser):
        page.go_to_create_delivery()
        page.go_to_cancel()
        page.cancel('leave')
        page.browser.implicitly_wait(0)
        page.should_not_be_delivery_creation("dis")

    def test_can_go_back_to_delivery_creation(self, browser):
        page.go_to_create_delivery()
        page.go_to_cancel()
        page.cancel('cancel')
        page.should_be_delivery_creation()


@pytest.mark.delivery
@pytest.mark.delivery_creation
class TestDeliveryCreation:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = AuthPage(browser, delivery_link)
        page.open()
        page.should_be_auth_page()
        email = os.getenv('SPRING_ADMIN_MAIL')
        password = os.getenv('SPRING_ADMIN_PASSWORD')
        page.auth(email, password)

        self.page = DeliveryPage(browser, delivery_link)
        time.sleep(1)
        self.page.open()

        self.page.should_be_create_delivery_button()

        self.delivery_number = f'AUTOTEST_{int(time.time())}'
        self.page.go_to_create_delivery()

        self.page.create_delivery(self.delivery_number)
        time.sleep(1)

    def test_can_see_delivery_draft_after_creation(self, browser):
        self.page.should_be_delivery_draft()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_delivery_creation("dis")

    def test_expected_delivery_info_equals_actual(self, browser):
        self.page.open()
        time.sleep(1)
        self.page.check_delivery_info(self.delivery_number)

    def test_expected_delivery_info_equals_actual_in_draft(self, browser):
        self.page.check_delivery_draft_info(self.delivery_number)

    def test_edit_and_save_see_summary(self, browser):
        sett = (f'EDITED_{self.delivery_number}', '30.03.2002')

        self.page.edit_delivery(*sett)
        self.page.save_delivery()

        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.check_delivery_info(*sett)

    def test_edit_and_save_see_draft(self, browser):
        sett = (f'EDITED_{self.delivery_number}', '30.03.2002')

        self.page.edit_delivery(*sett)
        self.page.save_delivery()

        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        time.sleep(1)
        self.page.check_delivery_draft_info(*sett)

    def test_edit_and_not_save_see_summary(self, browser):
        sett = (f'EDITED_{self.delivery_number}', '30.03.2002')

        self.page.edit_delivery(*sett)
        # self.page.save_delivery()    # не сохраняем!

        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.check_delivery_info(self.delivery_number)    # поэтому сверяем со старыми данными (дефолтными)

    def test_edit_and_not_save_see_draft(self, browser):
        sett = (f'EDITED_{self.delivery_number}', '30.03.2002')

        self.page.edit_delivery(*sett)
        # self.page.save_delivery()    # не сохраняем!

        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        time.sleep(1)
        self.page.check_delivery_draft_info(self.delivery_number)    # поэтому сверяем со старыми данными (дефолтными)

    def test_can_delete_delivery(self, browser):
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_delete_delivery()
        time.sleep(1)
        self.page.delete_delivery('delete')
        time.sleep(1)
        self.page.check_last_delivery(self.delivery_number, False)

    def test_can_cancel_delivery_deletion(self, browser):
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_delete_delivery()
        time.sleep(1)
        self.page.delete_delivery('cancel')
        time.sleep(1)
        self.page.check_last_delivery(self.delivery_number, True)


@pytest.mark.delivery_element
@pytest.mark.delivery_element_basis
class TestDeliveryElementBasis:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = AuthPage(browser, delivery_link)
        page.open()
        page.should_be_auth_page()
        email = os.getenv('SPRING_ADMIN_MAIL')
        password = os.getenv('SPRING_ADMIN_PASSWORD')
        page.auth(email, password)

        self.page = DeliveryPage(browser, delivery_link)
        time.sleep(1)
        self.page.open()

        self.page.should_be_create_delivery_button()
        self.delivery_number = f'AUTOTEST_{int(time.time())}'
        self.page.go_to_create_delivery()
        time.sleep(.5)
        self.page.create_delivery(self.delivery_number)
        time.sleep(1)

    def test_can_add_element(self, browser):
        self.page.should_be_delivery_draft()

    def test_can_see_element_creation(self, browser):
        self.page.should_be_delivery_draft()
        self.page.go_to_create_element()
        self.page.should_be_element_creation()

    def test_cant_see_element_creation(self, browser):
        self.page.should_be_delivery_draft()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('pres')

    def test_can_cancel_element_creation(self, browser):
        self.page.go_to_create_element()
        self.page.go_to_cancel_element()
        self.page.cancel('leave')
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('dis')

    def test_can_go_back_to_element_creation(self, browser):
        self.page.go_to_create_element()
        self.page.go_to_cancel_element()
        self.page.cancel('cancel')
        self.page.should_be_element_creation()


@pytest.mark.delivery_element
@pytest.mark.delivery_element_creation
class TestDeliveryElementCreation:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        page = AuthPage(browser, delivery_link)
        page.open()
        page.should_be_auth_page()
        email = os.getenv('SPRING_ADMIN_MAIL')
        password = os.getenv('SPRING_ADMIN_PASSWORD')
        page.auth(email, password)

        self.page = DeliveryPage(browser, delivery_link)
        time.sleep(1)
        self.page.open()
        time.sleep(1)
        self.page.should_be_create_delivery_button()
        self.delivery_number = f'AUTOTEST_{int(time.time())}'
        self.page.go_to_create_delivery()
        self.page.create_delivery(self.delivery_number)
        self.page.should_be_delivery_draft()
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(1)

    def test_can_see_delivery_draft_after_creation(self, browser):
        self.page.should_be_delivery_draft()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('dis')

    def test_expected_element_info_equals_actual(self, browser):
        time.sleep(2)
        self.page.check_element_info()

    def test_save_and_reload(self, browser):
        self.page.save_delivery()
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.should_be_any_element()

    def test_save_then_check(self, browser):
        self.page.save_delivery()
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        time.sleep(2)
        self.page.check_element_info()

    def test_not_save_and_reload(self, browser):
        # page.save_delivery()  # не сохраняем!
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_any_element()  # поэтому элементов не должно быть

    def test_delete_save_and_reload(self, browser):
        self.page.save_delivery()
        self.page.go_to_delete_element()
        self.page.delete_element('delete')
        self.page.save_delivery()
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.should_not_be_any_element()

    def test_delete_not_save_and_reload(self, browser):
        self.page.save_delivery()
        self.page.go_to_delete_element()
        self.page.delete_element('delete')
        # page.save_delivery()  # не сохраняем!
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.should_be_any_element()  # поэтому элемент должен остаться

    def test_can_cancel_deletion(self, browser):
        self.page.go_to_delete_element()
        self.page.delete_element('cancel')
        self.page.should_be_any_element()

    def test_can_add_few_elements(self, browser):
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(3)

    def test_can_add_few_elements_and_save(self, browser):
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(3)
        self.page.save_delivery()
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.count_elements(3)

    def test_can_add_few_elements_and_not_save(self, browser):
        time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(3)
        # page.save_delivery()  # не сохраняем!
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.should_not_be_any_element()  # поэтому элементов не должно быть

    def test_can_add_few_elements_and_save_then_add_few_elements_and_save(self, browser):
        time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(3)
        self.page.save_delivery()
        time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        self.page.count_elements(6)
        self.page.save_delivery()
        time.sleep(1)
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.count_elements(6)

    def test_can_add_few_elements_and_save_then_add_few_elements_and_not_save(self, browser):
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.count_elements(3)
        self.page.save_delivery()
        time.sleep(1)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.go_to_create_element()
        self.page.create_element()
        time.sleep(2)
        self.page.count_elements(6)
        # page.save_delivery()  # не сохраняем!
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.count_elements(3)  # поэтому элементов должно быть 3

    def test_can_edit_element(self):
        self.page.should_be_delivery_draft()
        self.page.should_be_any_element()

    def test_can_see_element_edit(self, browser):
        self.page.should_be_delivery_draft()
        self.page.should_be_any_element()
        self.page.go_to_edit_element()
        self.page.should_be_element_creation()

    def test_cant_see_element_edit(self, browser):
        self.page.should_be_delivery_draft()
        self.page.should_be_any_element()
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('pres')

    def test_can_cancel_element_edit(self, browser):
        self.page.go_to_edit_element()
        self.page.go_to_cancel_element()
        self.page.cancel('leave')
        self.page.browser.implicitly_wait(0)
        self.page.should_not_be_element_creation('dis')

    def test_can_go_back_to_element_edit(self, browser):
        self.page.go_to_edit_element()
        self.page.go_to_cancel_element()
        self.page.cancel('cancel')
        self.page.should_be_element_creation()

    def test_edit_element(self, browser):
        sett = ('Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration (0004)',
                '4', 'Склад 1', 'Ряд 1', 'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_delivery()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)

    def test_expected_edited_element_equals_actual(self, browser):
        sett = ('Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration (0004)',
                '4', 'Склад 1', 'Ряд 1', 'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        # self.page.save_delivery()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        sett = ('Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration',
                '4', 'Склад 1', 'Ряд 1', 'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.check_element_info(*sett)

    def test_edit_element_then_save_and_check(self, browser):
        sett = ('Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration (0004)',
                '4', 'Склад 1', 'Ряд 1', 'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_delivery()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        self.page.save_delivery()
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        sett = ('Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration',
                '4', 'Склад 1', 'Ряд 1', 'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')

        self.page.check_element_info(*sett)

    def test_edit_element_then_not_save_and_check(self, browser):
        sett = ('Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration (0004)',
                '4', 'Склад 1', 'Ряд 1', 'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_delivery()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        # page.save_delivery()  # не сохраняем!
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.check_element_info()  # поэтому сверяем со старыми данными (дефолтными)

    def test_edit_element_then_save_then_edit_element_then_save_and_check(self, browser):
        sett = ('Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration (0004)',
                '4', 'Склад 1', 'Ряд 1', 'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_delivery()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        sett = ('Dichtung DN 65, NBR (blau), 71x81x5,0mmDichtung DN 65, NBR (blau),'
                ' 71x81x5,0mm Alle Werkstoffe entsp... (0001)',
                '3', 'Lager of Magazine №2', 'Reihe 1', 'Stack 1', 'Board 1', 'Cell 1', 'Подяейка 1')
        self.page.save_delivery()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        self.page.save_delivery()
        self.page.check_element_info()
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        self.page.check_element_info()

    def test_edit_element_then_save_then_edit_element_then_not_save_and_check(self, browser):
        sett = ('Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration (0004)',
                '4', 'Склад 1', 'Ряд 1', 'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')
        self.page.save_delivery()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        sett = ('Dichtung DN 65, NBR (blau), 71x81x5,0mmDichtung DN 65, NBR (blau),'
                ' 71x81x5,0mm Alle Werkstoffe entsp... (0001)',
                '3', 'Lager of Magazine №2', 'Reihe 1', 'Stack 1', 'Board 1', 'Cell 1', 'Подяейка 1')
        self.page.save_delivery()
        self.page.go_to_edit_element()
        self.page.edit_element(*sett)
        # self.page.save_delivery()  # не сохраняем!
        time.sleep(2)
        self.page.check_element_info()
        DeliveryPage(browser, delivery_link).open()
        time.sleep(1)
        self.page.go_to_work()
        sett = ('Motoröl für FIAT 2015 Release der C-Serie in der maximalen Konfiguration',
                '4', 'Склад 1', 'Ряд 1', 'Стеллаж 1', 'Полка 1', 'Ячейка 1', 'erwer')

        self.page.check_element_info(*sett)
