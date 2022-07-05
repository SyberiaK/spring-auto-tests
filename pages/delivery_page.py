import datetime as dt
import time

from .work_page import WorkPage
from selenium.webdriver.common.keys import Keys
from .locators import WorkPageLocators, DeliveryPageLocators


class DeliveryPage(WorkPage):
    def should_be_create_delivery_button(self):
        assert self.is_element_present(*DeliveryPageLocators.CREATE_DELIVERY_BTN), \
            'Add delivery button is not presented'

    def should_be_delivery_creation(self):
        assert self.is_element_present(*DeliveryPageLocators.DELIVERY_DATE_INPUT), \
            'Delivery date input is not presented'
        assert self.is_element_present(*DeliveryPageLocators.DELIVERY_RESPONSIBLE_INPUT), \
            'Delivery responsible input is not presented'
        assert self.is_element_present(*DeliveryPageLocators.DELIVERY_SAVE_BTN), \
            'Delivery save button is not presented'

    def should_not_be_delivery_creation(self, pres_or_dis: str):
        if pres_or_dis == 'pres':
            assert self.is_not_element_present(*DeliveryPageLocators.DELIVERY_DATE_INPUT), \
                'Delivery date input is presented, but it shouldn\'t be'
            assert self.is_not_element_present(*DeliveryPageLocators.DELIVERY_RESPONSIBLE_INPUT), \
                'Delivery responsible input is presented, but it shouldn\'t be'
            assert self.is_not_element_present(*DeliveryPageLocators.DELIVERY_SAVE_BTN), \
                'Delivery save button is presented, but it shouldn\'t be'
        elif pres_or_dis == 'dis':
            assert self.is_disappeared(*DeliveryPageLocators.DELIVERY_DATE_INPUT), \
                'Delivery date input is presented, but it shouldn\'t be'
            assert self.is_disappeared(*DeliveryPageLocators.DELIVERY_RESPONSIBLE_INPUT), \
                'Delivery responsible input is presented, but it shouldn\'t be'
            assert self.is_disappeared(*DeliveryPageLocators.DELIVERY_SAVE_BTN), \
                'Delivery save button is presented, but it shouldn\'t be'

    def go_to_create_delivery(self):
        self.browser.find_element(*DeliveryPageLocators.CREATE_DELIVERY_BTN).click()

    def create_delivery(self,
                        responsible: str,
                        date: str = dt.date.today().strftime('%d.%m.%Y')):
        if date:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_DATE_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_DATE_INPUT).send_keys(date)
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_DATE_INPUT_LABEL).click()
            time.sleep(.5)
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_RESPONSIBLE_INPUT).send_keys(responsible)
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_SAVE_BTN).click()

    def go_to_cancel_delivery(self):
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_CLOSE_BTN).click()

    def check_last_delivery(self, responsible: str, is_here: bool = True):
        actual_responsible = self.browser.find_element(*DeliveryPageLocators.DELIVERY_INFO_RESPONSIBLE).text
        if is_here:
            assert actual_responsible == responsible, f'Delivery was deleted'
        else:
            assert actual_responsible != responsible, f'Delivery wasn\'t deleted'

    def check_delivery_info(self,
                            expected_responsible: str,
                            expected_date: str = dt.date.today().strftime("%d.%m.%Y")):
        actual_date = self.browser.find_element(*DeliveryPageLocators.DELIVERY_INFO_DATE).text
        actual_responsible = self.browser.find_element(*DeliveryPageLocators.DELIVERY_INFO_RESPONSIBLE).text

        assert actual_date == expected_date, f'Actual date: {actual_date}, ' \
                                             f'expected: {expected_date}'
        assert actual_responsible == expected_responsible, f'Actual responsible: {actual_responsible}, ' \
                                                           f'expected: {expected_responsible}'

    def should_be_delivery_draft(self):
        assert self.is_element_present(*DeliveryPageLocators.DELIVERY_DRAFT_DATE_INPUT), \
            'Delivery draft date input is not presented'
        assert self.is_element_present(*DeliveryPageLocators.DELIVERY_DRAFT_RESPONSIBLE_INPUT), \
            'Delivery draft responsible input is not presented'
        assert self.is_element_present(*DeliveryPageLocators.DELIVERY_DRAFT_SAVE_BTN), \
            'Delivery draft save button is not presented'
        assert self.is_element_present(*DeliveryPageLocators.DELIVERY_DRAFT_ADD_BTN), \
            'Delivery draft add element button is not presented'

    def should_not_be_delivery_draft(self):
        assert self.is_not_element_present(*DeliveryPageLocators.DELIVERY_DRAFT_DATE_INPUT), \
            'Delivery draft date input is not presented'
        assert self.is_not_element_present(*DeliveryPageLocators.DELIVERY_DRAFT_RESPONSIBLE_INPUT), \
            'Delivery draft responsible input is not presented'
        assert self.is_not_element_present(*DeliveryPageLocators.DELIVERY_DRAFT_SAVE_BTN), \
            'Delivery draft save button is not presented'
        assert self.is_not_element_present(*DeliveryPageLocators.DELIVERY_DRAFT_ADD_BTN), \
            'Delivery draft add element button is not presented'

    def check_delivery_draft_info(self,
                                  expected_responsible: str,
                                  expected_date: str = dt.date.today().strftime("%d.%m.%Y")):
        actual_date = self.browser.find_element(*DeliveryPageLocators.DELIVERY_DRAFT_DATE_INPUT)\
            .get_attribute('value')
        actual_responsible = self.browser.find_element(*DeliveryPageLocators.DELIVERY_DRAFT_RESPONSIBLE_INPUT)\
            .get_attribute('value')

        assert actual_date == expected_date, f'Actual date: {actual_date}, expected: {expected_date}'
        assert actual_responsible == expected_responsible, f'Actual responsible: {actual_responsible}, ' \
                                                           f'expected: {expected_responsible}'

    def edit_delivery(self,
                      responsible: str = None,
                      date: str = None):
        if not (responsible or date):
            raise AssertionError(f'No edit')
        if date:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_DRAFT_DATE_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_DRAFT_DATE_INPUT).send_keys(date)
        if responsible:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_DRAFT_RESPONSIBLE_INPUT)\
                .send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_DRAFT_RESPONSIBLE_INPUT).send_keys(responsible)

    def save_delivery(self):
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_DRAFT_SAVE_BTN).click()
        time.sleep(2)

    def go_to_delivery(self):
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_INFO).click()

    def go_to_delete_delivery(self):
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_DELETE_BTN).click()

    def delete_delivery(self,
                        dec: str):
        if dec == 'cancel':
            self.browser.find_element(*WorkPageLocators.MSGBOX2_CANCEL_BTN).click()
        elif dec == 'delete':
            self.browser.find_element(*WorkPageLocators.MSGBOX2_DELETE_BTN).click()
        else:
            raise AssertionError('Wrong decision (decisions available: cancel, leave)')

    def should_be_element_creation(self):
        assert self.is_element_present(
            *DeliveryPageLocators.DELIVERY_ELEM_PRODUCT_INPUT), 'Element product input is not presented'
        assert self.is_element_present(
            *DeliveryPageLocators.DELIVERY_ELEM_COUNT_INPUT), 'Element count input is not presented'
        assert self.is_element_present(
            *DeliveryPageLocators.DELIVERY_ELEM_STORAGE_INPUT), 'Element storage input is not presented'
        assert self.is_element_present(
            *DeliveryPageLocators.DELIVERY_ELEM_ROW_INPUT), 'Element row input is not presented'
        assert self.is_element_present(
            *DeliveryPageLocators.DELIVERY_ELEM_STACK_INPUT), 'Element stack input is not presented'
        assert self.is_element_present(
            *DeliveryPageLocators.DELIVERY_ELEM_BOARD_INPUT), 'Element board input is not presented'
        assert self.is_element_present(
            *DeliveryPageLocators.DELIVERY_ELEM_CELL_INPUT), 'Element cell input is not presented'
        assert self.is_element_present(
            *DeliveryPageLocators.DELIVERY_ELEM_SAVE_BTN), 'Element save button is not presented'
    
    def should_not_be_element_creation(self, pres_or_dis: str):
        if pres_or_dis == 'pres':
            assert self.is_not_element_present(
                *DeliveryPageLocators.DELIVERY_ELEM_PRODUCT_INPUT), \
                'Element product input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *DeliveryPageLocators.DELIVERY_ELEM_COUNT_INPUT), 'Element count input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *DeliveryPageLocators.DELIVERY_ELEM_STORAGE_INPUT), \
                'Element storage input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *DeliveryPageLocators.DELIVERY_ELEM_ROW_INPUT), 'Element row input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *DeliveryPageLocators.DELIVERY_ELEM_STACK_INPUT), 'Element stack input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *DeliveryPageLocators.DELIVERY_ELEM_BOARD_INPUT), 'Element board input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *DeliveryPageLocators.DELIVERY_ELEM_CELL_INPUT), 'Element cell input is presented, but it shouldn\'t'
            assert self.is_not_element_present(
                *DeliveryPageLocators.DELIVERY_ELEM_SAVE_BTN), 'Element save button is presented, but it shouldn\'t'
        elif pres_or_dis == 'dis':
            assert self.is_disappeared(
                *DeliveryPageLocators.DELIVERY_ELEM_PRODUCT_INPUT), \
                'Element product input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *DeliveryPageLocators.DELIVERY_ELEM_COUNT_INPUT), 'Element count input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *DeliveryPageLocators.DELIVERY_ELEM_STORAGE_INPUT), \
                'Element storage input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *DeliveryPageLocators.DELIVERY_ELEM_ROW_INPUT), 'Element row input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *DeliveryPageLocators.DELIVERY_ELEM_STACK_INPUT), 'Element stack input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *DeliveryPageLocators.DELIVERY_ELEM_BOARD_INPUT), 'Element board input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *DeliveryPageLocators.DELIVERY_ELEM_CELL_INPUT), 'Element cell input is presented, but it shouldn\'t'
            assert self.is_disappeared(
                *DeliveryPageLocators.DELIVERY_ELEM_SAVE_BTN), 'Element save button is presented, but it shouldn\'t'
    
    def go_to_create_element(self):
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_DRAFT_ADD_BTN).click()
    
    def create_element(self,
                       product: str = 'Dichtung DN 65, NBR (blau), '
                                      '71x81x5,0mmDichtung DN 65, NBR (blau),'
                                      ' 71x81x5,0mm Alle Werkstoffe entsp... (0001)',
                       count: int = 3,
                       storage: str = 'Lager of Magazine №2',
                       row: str = 'Reihe 1',
                       stack: str = 'Stack 1',
                       board: str = 'Board 1',
                       cell: str = 'Cell 1'):
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_PRODUCT_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT))):
            if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].text == product:
                self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No product found with this name: {product}')
        time.sleep(1)

        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_COUNT_INPUT).send_keys(str(count))

        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_STORAGE_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT))):
            if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].text == storage:
                self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No storage found with this name: {storage}')

        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_ROW_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == row:
                self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No row found with this name: {row}')

        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_STACK_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == stack:
                self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No stack found with this name: {stack}')

        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_BOARD_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == board:
                self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No board found with this name: {board}')

        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_CELL_INPUT).click()
        time.sleep(2)
        for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN))):
            if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == cell:
                self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                break
        else:
            raise AssertionError(f'No cell found with this name: {cell}')

        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_SAVE_BTN).click()

    def go_to_cancel_element(self):
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_CLOSE_BTN).click()

    def check_element_info(self,
                           expected_product: str = 'Dichtung DN 65, NBR (blau), 71x81x5,0mmDichtung DN 65, NBR (blau),'
                                                   ' 71x81x5,0mm Alle Werkstoffe entsp... (0001)',
                           expected_count: str = '3',
                           expected_storage: str = 'Lager of Magazine №2',
                           expected_row: str = 'Reihe 1',
                           expected_stack: str = 'Stack 1',
                           expected_board: str = 'Board 1',
                           expected_cell: str = 'Cell 1'):
        actual_product = self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_INFO_PRODUCT).text
        actual_count = self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_INFO_COUNT).text
        actual_storage = self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_INFO_STORAGE).text
        actual_row = self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_INFO_ROW).text
        actual_stack = self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_INFO_STACK).text
        actual_board = self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_INFO_BOARD).text
        actual_cell = self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_INFO_CELL).text

        assert actual_product == expected_product, f'Actual product: {actual_product}, expected: {expected_product}'
        assert actual_count == expected_count, f'Actual count: {actual_count}, expected: {expected_count}'
        assert actual_storage == expected_storage, f'Actual storage: {actual_storage}, expected: {expected_storage}'
        assert actual_row == expected_row, f'Actual row: {actual_row}, expected: {expected_row}'
        assert actual_stack == expected_stack, f'Actual stack: {actual_stack}, expected: {expected_stack}'
        assert actual_board == expected_board, f'Actual board: {actual_board}, expected: {expected_board}'
        assert actual_cell == expected_cell, f'Actual cell: {actual_cell}, expected: {expected_cell}'

    def should_be_any_element(self):
        assert self.is_element_present(*DeliveryPageLocators.DELIVERY_ELEM_INFO), f'No element found'

    def should_not_be_any_element(self):
        assert self.is_not_element_present(
            *DeliveryPageLocators.DELIVERY_ELEM_INFO), f'Element was found, but it shouldn\'t be'

    def go_to_delete_element(self):
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_DRAFT_DELETE_ELEM_BTN).click()

    def count_elements(self, count: int):
        elements = self.browser.find_elements(*DeliveryPageLocators.DELIVERY_ELEM_INFO)
        assert len(elements) == count, f'Actual number of elements is {len(elements)}, expected: {count}'

    def go_to_edit_element(self):
        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_INFO).click()

    def edit_element(self,
                     product: str = None,
                     count: int = None,
                     storage: str = None,
                     row: str = None,
                     stack: str = None,
                     board: str = None,
                     cell: str = None):
        if not (product or count or storage or row or stack or board or cell):
            raise AssertionError(f'No edit')
        if product:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_PRODUCT_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_PRODUCT_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_PRODUCT_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT))):
                if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].text == product:
                    self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No product found with this name: {product}')
            time.sleep(1)
        if count:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_COUNT_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_COUNT_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_COUNT_INPUT).send_keys(str(count))
        if storage:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_STORAGE_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_STORAGE_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_STORAGE_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT))):
                if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].text == storage:
                    self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No storage found with this name: {storage}')
        if row:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_ROW_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_ROW_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_ROW_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == row:
                    self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No row found with this name: {row}')
        if stack:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_STACK_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_STACK_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_STACK_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == stack:
                    self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No stack found with this name: {stack}')
        if board:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_BOARD_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_BOARD_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_BOARD_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == board:
                    self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No board found with this name: {board}')
        if cell:
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_CELL_INPUT).send_keys(Keys.CONTROL + "a")
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_CELL_INPUT).send_keys(Keys.DELETE)
            self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_CELL_INPUT).click()
            time.sleep(2)
            for i in range(len(self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN))):
                if self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT_SPAN)[i].text == cell:
                    self.browser.find_elements(*DeliveryPageLocators.DROPDOWN_CONTENT)[i].click()
                    break
            else:
                raise AssertionError(f'No cell found with this name: {cell}')

        self.browser.find_element(*DeliveryPageLocators.DELIVERY_ELEM_SAVE_BTN).click()
