from selenium.webdriver.common.by import By


class BasePageLocators:
    """LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")"""


class WorkPageLocators:
    MSGBOX_CANCEL_BTN = (By.ID, 'msgbox-cancel-btn')
    MSGBOX_LEAVE_BTN = (By.ID, 'msgbox-leave-btn')
    MSGBOX_FORCECLOSE_BTN = (By.ID, 'msgbox-forceclose-btn')


class AuthPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, '.email input')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.password input')
    LOGIN_SUBMIT = (By.CSS_SELECTOR, 'button .login')


class OrderPageLocators:
    CREATE_ORDER_BTN = (By.ID, 'order-create-btn')

    ORDER_NUMBER_INPUT = (By.ID, 'order-number-input')
    ORDER_DATE_INPUT = (By.ID, 'order-date-input')
    ORDER_SHOP_INPUT = (By.ID, 'order-shop-input')
    ORDER_SHOP_DROPDOWN = (By.ID, 'order-shop-dropdown')
    ORDER_SHOP_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-shop-dropdown li')
    ORDER_SHOP_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-shop-dropdown li > span')
    ORDER_PROVIDER_INPUT = (By.ID, 'order-provider-input')
    ORDER_PROVIDER_DROPDOWN = (By.ID, 'order-provider-dropdown')
    ORDER_PROVIDER_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-provider-dropdown li')
    ORDER_PROVIDER_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-provider-dropdown li > span')
    ORDER_SAVE_BTN = (By.ID, 'order-save-btn')
    ORDER_CLOSE_BTN = (By.ID, 'order-close-btn')

    ORDER_INFO = (By.CSS_SELECTOR, 'tbody tr')
    ORDER_INFO_NUMBER = (By.XPATH, '//tbody/tr[1]/td[1]//span/span')
    ORDER_INFO_DATE = (By.XPATH, '//tbody/tr[1]/td[2]//span/span')
    ORDER_INFO_PROVIDER = (By.XPATH, '//tbody/tr[1]/td[3]//span/span')
    ORDER_INFO_NETTO = (By.XPATH, '//tbody/tr[1]/td[4]//span/span')
    ORDER_INFO_STATUS = (By.XPATH, '//tbody/tr[1]/td[5]//span/span')

    ORDER_DRAFT_NUMBER_INPUT = (By.ID, 'order-draft-number-input')
    ORDER_DRAFT_DATE_INPUT = (By.ID, 'order-draft-date-input')
    ORDER_DRAFT_SHOP_INPUT = (By.ID, 'order-draft-shop-input')
    ORDER_DRAFT_SHOP_DROPDOWN = (By.ID, 'order-shop-dropdown')
    ORDER_DRAFT_SHOP_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-shop-dropdown li')
    ORDER_DRAFT_SHOP_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-shop-dropdown li > span')
    ORDER_DRAFT_PROVIDER_INPUT = (By.ID, 'order-draft-provider-input')
    ORDER_DRAFT_PROVIDER_DROPDOWN = (By.ID, 'order-provider-dropdown')
    ORDER_DRAFT_PROVIDER_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-provider-dropdown li')
    ORDER_DRAFT_PROVIDER_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-provider-dropdown li > span')
    ORDER_DRAFT_DOWNLOAD_BTN = (By.ID, 'order-draft-download-btn')
    ORDER_DRAFT_CANCEL_BTN = (By.ID, 'order-draft-cancel-btn')
    ORDER_DRAFT_FINISH_BTN = (By.ID, 'order-draft-finish-btn')
    ORDER_DRAFT_SAVE_BTN = (By.ID, 'order-draft-save-btn')
    ORDER_DRAFT_ADD_BTN = (By.ID, 'order-draft-add-btn')
    ORDER_DRAFT_DELETE_ELEM_BTN = (By.ID, 'order-draft-delete-elem-btn')
