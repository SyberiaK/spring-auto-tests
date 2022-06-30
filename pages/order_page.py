from work_page import WorkPage
from locators import WorkPageLocators, OrderPageLocators
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

    def go_to_create_order(self):
        self.browser.find_element(*OrderPageLocators.CREATE_ORDER_BTN).click()

    def create_order(self,
                     number: str,
                     date: str = dt.date.today().strftime("%d.%m.%Y"),
                     shop: str = 'Magazine №2',
                     provider: str = 'Firma Regress'):
        self.browser.find_element(*OrderPageLocators.CREATE_ORDER_BTN).click()
        self.browser.find_element(*OrderPageLocators.ORDER_NUMBER_INPUT).send_keys(number)
        if date:
            self.browser.find_element(*OrderPageLocators.ORDER_DATE_INPUT).send_keys(date)
        self.browser.find_element(*OrderPageLocators.ORDER_SHOP_INPUT).click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
            if v.text == shop:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No shop found with this name: {shop}')
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
            if v.text == provider:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No provider found with this name: {provider}')
        self.browser.find_element(*OrderPageLocators.ORDER_SAVE_BTN).click()

    def go_to_cancel_order(self):
        self.browser.find_element(*OrderPageLocators.ORDER_CLOSE_BTN).click()

    def cancel(self,
               dec: str):
        if dec == 'cancel':
            self.browser.find_element(*WorkPageLocators.MSGBOX_CANCEL_BTN).click()
        elif dec == 'leave':
            self.browser.find_element(*WorkPageLocators.MSGBOX_LEAVE_BTN).click()
        elif dec == 'forceclose':
            self.browser.find_element(*WorkPageLocators.MSGBOX_FORCECLOSE_BTN).click()
        else:
            raise AssertionError('Wrong decision (decisions avaliable: cancel, leave, forceclose)')

    def check_last_order_after_cancel(self,
                                      number: str):
        actual_number = self.browser.find_element(*OrderPageLocators.ORDER_INFO_NUMBER).text
        assert actual_number != number, f'Order was created after cancel'

    def check_order_info(self,
                         expected_number: str,
                         expected_date: str = dt.date.today().strftime("%d.%m.%Y"),
                         expected_provider: str = 'Firma Regress',
                         expected_netto: str = '0',
                         expected_status: str = 'Draft'):
        actual_number = self.browser.find_element(*OrderPageLocators.ORDER_INFO_NUMBER).text
        actual_date = self.browser.find_element(*OrderPageLocators.ORDER_INFO_DATE).text
        actual_provider = self.browser.find_element(*OrderPageLocators.ORDER_INFO_PROVIDER).text
        actual_netto = self.browser.find_element(*OrderPageLocators.ORDER_INFO_NETTO).text
        actual_status = self.browser.find_element(*OrderPageLocators.ORDER_INFO_STATUS).text

        assert actual_number == expected_number, f'Actual number: {actual_number}, expected: {expected_number}'
        assert actual_date == expected_date, f'Actual date: {actual_date}, expected: {expected_date}'
        assert actual_provider == expected_provider, f'Actual provider: {actual_provider}, expected: {expected_provider}'
        assert actual_netto == expected_netto, f'Actual netto: {actual_netto}, expected: {expected_netto}'
        assert actual_status == expected_status, f'Actual status: {actual_status}, expected: {expected_status}'

        if actual_status == 'Finished':
            self.go_to_order()
            finish_btn_state = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN).get_attribute(
                "disabled")
            cancel_btn_state = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN).get_attribute(
                "disabled")
            save_btn_state = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN).get_attribute(
                "disabled")
            add_btn_state = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_ADD_BTN).get_attribute(
                "disabled")
            assert finish_btn_state == "true", 'Finish button is not disabled, but it should be'
            assert cancel_btn_state == "true", 'Cancel button is not disabled, but it should be'
            assert save_btn_state == "true", 'Save button is not disabled, but it should be'
            assert add_btn_state == "true", 'Add button is not disabled, but it should be'

    def should_be_order_draft(self):
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT), \
            'Order draft number input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT), \
            'Order draft date input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT), \
            'Order draft shop input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT), \
            'Order draft provider input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_DOWNLOAD_BTN), \
            'Order draft download button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN), \
            'Order draft cancel button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN), \
            'Order draft finish button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN), \
            'Order draft save button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_ADD_BTN), \
            'Order draft add elem button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_DRAFT_DELETE_ELEM_BTN), \
            'Order draft delete elem button is not presented'

    def should_not_be_order_draft(self):
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT), \
            'Order draft number input is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT), \
            'Order draft date input is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT), \
            'Order draft shop input is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT), \
            'Order draft provider input is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_DOWNLOAD_BTN), \
            'Order draft download button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN), \
            'Order draft cancel button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN), \
            'Order draft finish button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN), \
            'Order draft save button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_ADD_BTN), \
            'Order draft add elem button is not presented'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_DRAFT_DELETE_ELEM_BTN), \
            'Order draft delete elem button is not presented'

    def check_order_draft_info(self,
                               expected_number: str,
                               expected_date=dt.date.today().strftime("%d.%m.%Y"),
                               expected_shop: str = 'Magazine №2',
                               expected_provider: str = 'Firma Regress'):
        actual_number = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT).text
        actual_date = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_DATE_INPUT).text
        actual_shop = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT).text
        actual_provider = self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT).text

        assert actual_number == expected_number, f'Actual number: {actual_number}, expected: {expected_number}'
        assert actual_date == expected_date, f'Actual date: {actual_date}, expected: {expected_date}'
        assert actual_shop == expected_shop, f'Actual number: {actual_shop}, expected: {expected_shop}'
        assert actual_provider == expected_provider, f'Actual number: {actual_provider}, expected: {expected_provider}'

    def edit_order_field(self,
                         field: str,
                         data: str):
        if field == 'number':
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT).clear().send_keys(data)
        elif field == 'date':
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_NUMBER_INPUT).clear().send_keys(data)
        elif field == 'shop':
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_SHOP_INPUT).click()
            for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
                if v.text == data:
                    self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No shop found with this name: {data}')
        elif field == 'provider':
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_PROVIDER_INPUT).click()
            for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
                if v.text == data:
                    self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No provider found with this name: {data}')
        else:
            raise AssertionError(f'Wrong field (fields avaliable: number, date, shop, provider)')

    def save_order(self):
        self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_SAVE_BTN).click()

    def go_to_order(self):
        self.browser.find_element(*OrderPageLocators.ORDER_INFO).click()

    def change_order_status(self,
                            status: str):
        if status == 'finish':
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_FINISH_BTN).click()
        elif status == 'cancel':
            self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_CANCEL_BTN).click()
        else:
            raise AssertionError(f'Wrong status (statuses avaliable: finish, cancel)')

    def should_be_element_creation(self):
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_TYPE_INPUT), 'Element type input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT), 'Element product input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_COUNT_INPUT), 'Element count input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT), 'Element account input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT), 'Element MVZ input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_INNER_INPUT), 'Element inner order input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_PRICE_INPUT), 'Element price input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_STORAGE_INPUT), 'Element storage input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_ROW_INPUT), 'Element row input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_STACK_INPUT), 'Element stack input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_BOARD_INPUT), 'Element board input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_CELL_INPUT), 'Element cell input is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_SAVE_BTN), 'Element save button is not presented'
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_CLOSE_BTN), 'Element close button is not presented'

    def should_not_be_element_creation(self):
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_TYPE_INPUT), 'Element type input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT), 'Element product input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_COUNT_INPUT), 'Element count input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT), 'Element account input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT), 'Element MVZ input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_INNER_INPUT), 'Element inner order input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_PRICE_INPUT), 'Element price input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_STORAGE_INPUT), 'Element storage input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_ROW_INPUT), 'Element row input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_STACK_INPUT), 'Element stack input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_BOARD_INPUT), 'Element board input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_CELL_INPUT), 'Element cell input is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_SAVE_BTN), 'Element save button is presented, but it shouldn\'t'
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_CLOSE_BTN), 'Element close button is presented, but it shouldn\'t'

    def go_to_create_element(self):
        self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_ADD_BTN).click()

    def create_element(self, ttype: str = 'K',
                       product: str = 'Dichtung DN 65, NBR (blau), 71x81x5,0mmDichtung DN 65,'
                                      ' NBR (blau), 71x81x5,0mm Alle Werkstoffe entsprechen den'
                                      ' Anforderungen der Verordnungen FDA 21 CFR 177.2600, bzw.'
                                      ' FDA 21 CFR 177.1550 und (EG) 1935/2004 Art.-Nr.: 3814 (0001)',
                       count: int = 3,
                       account: str = 'Regress sachkonto (003)',
                       mvz: str = 'Double Regress MVZ (001)',
                       inner: str = 'Double regress inner order (001)',
                       price: float = 16.00,
                       storage: str = 'Lager of Magazine №2',
                       row: str = 'Reihe 1',
                       stack: str = 'Stack 1',
                       board: str = 'Board 1',
                       cell: str = 'Cell 1'):
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_TYPE_INPUT).click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
            if v.text == ttype:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No element type found with this name: {ttype}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRODUCT_INPUT).click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT):
            if v.text == product:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No product found with this name: {product}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_COUNT_INPUT).send_keys(str(count))

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ACCOUNT_INPUT).clear().click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT):
            if v.text == account:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No account found with this name: {account}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_MVZ_INPUT).clear().click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT):
            if v.text == mvz:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No MVZ found with this name: {mvz}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INNER_INPUT).clear().click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT):
            if v.text == inner:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No inner order found with this name: {inner}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_PRICE_INPUT).clear().send_keys(str(price))

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_STORAGE_INPUT).click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
            if v.text == storage:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No storage found with this name: {storage}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_ROW_INPUT).click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
            if v.text == row:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No row found with this name: {row}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_STACK_INPUT).click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
            if v.text == stack:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No stack found with this name: {stack}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_BOARD_INPUT).click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
            if v.text == board:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No board found with this name: {board}')

        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_CELL_INPUT).click()
        for i, v in self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT_SPAN):
            if v.text == cell:
                self.browser.find_elements(*OrderPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No cell found with this name: {cell}')

        self.browser.find_element(*OrderPageLocators.ORDER_SAVE_BTN).click()

    def go_to_cancel_element(self):
        self.browser.find_element(*OrderPageLocators.ORDER_ELEM_CLOSE_BTN).click()

    def check_element_info(self,
                           expected_type: str = 'K',
                           expected_account: str = 'Regress sachkonto',
                           expected_mvz: str = 'Double Regress MVZ',
                           expected_inner: str = 'Double regress inner order',
                           expected_product: str = 'Dichtung DN 65, NBR (blau), 71x81x5,0mmDichtung DN 65,'
                                                   ' NBR (blau), 71x81x5,0mm Alle Werkstoffe entsprechen den'
                                                   ' Anforderungen der Verordnungen FDA 21 CFR 177.2600, bzw.'
                                                   ' FDA 21 CFR 177.1550 und (EG) 1935/2004 Art.-Nr.: 3814',
                           expected_count: int = 3,
                           expected_netto: float = 48.00,
                           expected_price: float = 16.00,
                           expected_unit: str = 'Stuck'):
        actual_type = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_TYPE).text
        actual_account = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_ACCOUNT).text
        actual_mvz = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_MVZ).text
        actual_inner = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_INNER).text
        actual_product = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_PRODUCT).text
        actual_count = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_COUNT).text
        actual_netto = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_NETTO).text
        actual_price = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_PRICE).text
        actual_unit = self.browser.find_element(*OrderPageLocators.ORDER_ELEM_INFO_UNIT).text

        assert actual_type == expected_type, f'Actual type: {actual_type}, expected: {expected_type}'
        assert actual_account == expected_account, f'Actual account: {actual_account}, expected: {expected_account}'
        assert actual_mvz == expected_mvz, f'Actual MVZ: {actual_mvz}, expected: {expected_mvz}'
        assert actual_inner == expected_inner, f'Actual inner order: {actual_inner}, expected: {expected_inner}'
        assert actual_product == expected_product, f'Actual product: {actual_product}, expected: {expected_product}'
        assert actual_count == expected_count, f'Actual count: {actual_count}, expected: {expected_count}'
        assert actual_netto == expected_netto, f'Actual netto: {actual_netto}, expected: {expected_netto}'
        assert actual_price == expected_price, f'Actual price: {actual_price}, expected: {expected_price}'
        assert actual_unit == expected_unit, f'Actual unit: {actual_unit}, expected: {expected_unit}'

    def should_be_any_element(self):
        assert self.is_element_present(*OrderPageLocators.ORDER_ELEM_INFO), f'No element found'

    def should_not_be_any_element(self):
        assert self.is_not_element_present(*OrderPageLocators.ORDER_ELEM_INFO), f'Element was found, but it shouldn\'t be'

    def go_to_delete_element(self):
        self.browser.find_element(*OrderPageLocators.ORDER_DRAFT_DELETE_ELEM_BTN).click()

    def delete_element(self,
                       dec: str):
        if dec == 'cancel':
            self.browser.find_element(*WorkPageLocators.MSGBOX_CANCEL_BTN).click()
        elif dec == 'delete':
            self.browser.find_element(*WorkPageLocators.MSGBOX_DELETE_BTN).click()
        elif dec == 'forceclose':
            self.browser.find_element(*WorkPageLocators.MSGBOX_FORCECLOSE_BTN).click()
        else:
            raise AssertionError('Wrong decision (decisions avaliable: cancel, leave, forceclose)')

    def count_elements(self, count: int):
        elements = self.browser.find_elements(*OrderPageLocators.ORDER_ELEM_INFO)
        assert len(elements) == count, f'Actual number of elements is {len(elements)}, expected: {count}'
