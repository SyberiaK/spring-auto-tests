from .work_page import WorkPage
from .locators import WorkPageLocators, OrderPageLocators
import datetime as dt

class OrderPage(WorkPage):
    def should_be_create_order_button(self):
        assert self.is_element_present(*OrderPageLocators.CREATE_ORDER_BTN), 'Add order button is not presented'

    def should_be_order_creation(self):
        assert self.is_element_present(*OrderPageLocators.ORDER_NUMBER_INPUT), 'Order number input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DATE_INPUT), 'Order date input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_SHOP_INPUT), 'Order shop input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_PROVIDER_INPUT), 'Order provider input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_SAVE_BTN), 'Order save button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_CLOSE_BTN), 'Order close button is not presented'

    def should_not_be_order_creation(self):
        assert self.is_not_element_present(*OrderPageLocators.ORDER_NUMBER_INPUT), 'Order number input is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DATE_INPUT), 'Order date input is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_SHOP_INPUT), 'Order shop input is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_PROVIDER_INPUT), 'Order provider input is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_SAVE_BTN), 'Order save button is presented, but it shouldn\'t be'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_CLOSE_BTN), 'Order close button is presented, but it shouldn\'t be'

    def add_order(self, number, date=None, shop='Magazine №2', provider='Firma Regress'):
        self.browser.find_element(*OrderPageLocators.CREATE_ORDER_BTN).click()
        self.browser.find_element(*OrderPageLocators.ORDER_NUMBER_INPUT).send_keys(number)
        if date:
            self.browser.find_element(*OrderPageLocators.ORDER_DATE_INPUT).send_keys(date)
        self.browser.find_element(*OrderPageLocators.ORDER_SHOP_INPUT).click()
        for i, v in self.browser.find_elements(*OrderPageLocators.ORDER_SHOP_DROPDOWN_CONTENT_SPAN):
            if v.text == shop:
                self.browser.find_elements(*OrderPageLocators.ORDER_SHOP_DROPDOWN_CONTENT)[i].click()
                break
        for i, v in self.browser.find_elements(*OrderPageLocators.ORDER_PROVIDER_DROPDOWN_CONTENT_SPAN):
            if v.text == provider:
                self.browser.find_elements(*OrderPageLocators.ORDER_PROVIDER_DROPDOWN_CONTENT)[i].click()
                break
        self.browser.find_element(*OrderPageLocators.ORDER_SAVE_BTN).click()

    def cancel_order(self, dec):
        self.browser.find_element(*OrderPageLocators.CREATE_ORDER_BTN).click()
        self.browser.find_element(*OrderPageLocators.ORDER_CLOSE_BTN).click()
        if dec == 'cancel':
            self.browser.find_element(*WorkPageLocators.MSGBOX_CANCEL_BTN).click()
        elif dec == 'leave':
            self.browser.find_element(*WorkPageLocators.MSGBOX_LEAVE_BTN).click()
        elif dec == 'forceclose':
            self.browser.find_element(*WorkPageLocators.MSGBOX_FORCECLOSE_BTN).click()
        else:
            raise AssertionError('Bad decidion (not in ("cancel", "leave", "forceclose"))')

    def check_order_info(self):



    def should_be_order_draft(self):
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT), 'Order draft number input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT), 'Order draft date input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT), 'Order draft shop input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT), 'Order draft provider input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_DOWNLOAD_BTN), 'Order draft download button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN), 'Order draft cancel button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN), 'Order draft finish button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN), 'Order draft save button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_ADD_BTN), 'Order draft add elem button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_DELETE_ELEM_BTN), 'Order draft delete elem button is not presented'

    def should_not_be_order_draft(self):
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT), 'Order draft number input is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT), 'Order draft date input is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT), 'Order draft shop input is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT), 'Order draft provider input is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_DOWNLOAD_BTN), 'Order draft download button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN), 'Order draft cancel button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN), 'Order draft finish button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN), 'Order draft save button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_ADD_BTN), 'Order draft add elem button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_DELETE_ELEM_BTN), 'Order draft delete elem button is not presented'

    def check_order_draft_info(self, expected_number, expected_date=None, expected_shop='Magazine №2', expected_provider='Firma Regress'):
        actual_number = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT).text
        assert actual_number == expected_number, f'Actual number: {actual_number}, expected: {expected_number}'
        actual_date = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT).text
        if not expected_date:
            expected_date = dt.date.today()
        assert actual_date == expected_date, f'Actual date: {actual_date}, expected: {expected_date}'
        actual_shop = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT).text
        assert actual_shop == expected_shop, f'Actual number: {actual_shop}, expected: {expected_shop}'
        actual_provider = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT).text
        assert actual_provider == expected_provider, f'Actual number: {actual_provider}, expected: {expected_provider}'

