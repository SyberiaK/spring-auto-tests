from .base_page import BasePage
from .locators import WorkPageLocators


class WorkPage(BasePage):
    def cancel(self,
               dec: str):
        if dec == 'cancel':
            self.browser.find_element(*WorkPageLocators.MSGBOX_CANCEL_BTN).click()
        elif dec == 'leave':
            self.browser.find_element(*WorkPageLocators.MSGBOX_LEAVE_BTN).click()
        else:
            raise AssertionError('Wrong decision (decisions avaliable: cancel, leave)')

    def delete_element(self,
                       dec: str):
        if dec == 'cancel':
            self.browser.find_element(*WorkPageLocators.MSGBOX2_CANCEL_BTN).click()
        elif dec == 'delete':
            self.browser.find_element(*WorkPageLocators.MSGBOX2_DELETE_BTN).click()
        else:
            raise AssertionError('Wrong decision (decisions available: cancel, delete)')