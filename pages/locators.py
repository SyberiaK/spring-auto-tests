from selenium.webdriver.common.by import By


class BasePageLocators:
    """LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")"""


class WorkPageLocators:
    MSGBOX_CANCEL_BTN = (By.CSS_SELECTOR, '.msgbox-cancel-btn')
    MSGBOX_LEAVE_BTN = (By.CSS_SELECTOR, '.msgbox-leave-btn')
    MSGBOX2_CANCEL_BTN = (By.CSS_SELECTOR, '.el-button--default.el-button--small')
    MSGBOX2_DELETE_BTN = (By.CSS_SELECTOR, '.el-button--small.is-plain')

    WORK_INFO = (By.CSS_SELECTOR, 'tbody tr')

    WORK_CLOSE_BTN = (By.CSS_SELECTOR, 'button.el-dialog__headerbtn')

    WORK_ELEM_INFO = (By.CSS_SELECTOR, 'div.AppTable tbody tr')

    DROPDOWN_CONTENT = (By.XPATH, '//div[@aria-hidden="false"]//li')
    DROPDOWN_CONTENT_SPAN = (By.XPATH, '//div[@aria-hidden="false"]//li/span')  # для некоторых полей


class AuthPageLocators:
    EMAIL_INPUT = (By.CSS_SELECTOR, '.email input')
    PASSWORD_INPUT = (By.CSS_SELECTOR, '.password input')
    LOGIN_BTN = (By.CSS_SELECTOR, 'button.login')


class OrderPageLocators:
    CREATE_ORDER_BTN = (By.ID, 'order-create-btn')

    # order creation
    ORDER_NUMBER_INPUT = (By.CSS_SELECTOR, '#order-number-input input')
    ORDER_DATE_INPUT = (By.CSS_SELECTOR, '#order-date-input input')
    ORDER_SHOP_INPUT = (By.CSS_SELECTOR, '#order-shop-input input')
    ORDER_PROVIDER_INPUT = (By.CSS_SELECTOR, '#order-provider-input input')
    ORDER_SAVE_BTN = (By.ID, 'order-save-btn')

    # order info
    ORDER_INFO_NUMBER = (By.XPATH, '//tbody/tr[1]/td[1]//span/span')
    ORDER_INFO_DATE = (By.XPATH, '//tbody/tr[1]/td[2]//span/span')
    ORDER_INFO_PROVIDER = (By.XPATH, '//tbody/tr[1]/td[3]//span/span')
    ORDER_INFO_NETTO = (By.XPATH, '//tbody/tr[1]/td[4]//span/span')
    ORDER_INFO_STATUS = (By.XPATH, '//tbody/tr[1]/td[5]//span/span')

    # order draft
    ORDER_DRAFT_NUMBER_INPUT = (By.CSS_SELECTOR, '#order-draft-number-input input')
    ORDER_DRAFT_DATE_INPUT = (By.CSS_SELECTOR, '#order-draft-date-input input')
    ORDER_DRAFT_SHOP_INPUT = (By.CSS_SELECTOR, '#order-draft-shop-input input')
    ORDER_DRAFT_PROVIDER_INPUT = (By.CSS_SELECTOR, '#order-draft-provider-input input')
    ORDER_DRAFT_DOWNLOAD_BTN = (By.ID, 'order-draft-download-btn')
    ORDER_DRAFT_CANCEL_BTN = (By.ID, 'order-draft-cancel-btn')
    ORDER_DRAFT_FINISH_BTN = (By.ID, 'order-draft-finish-btn')
    ORDER_DRAFT_SAVE_BTN = (By.ID, 'order-draft-save-btn')
    ORDER_DRAFT_ADD_BTN = (By.ID, 'order-draft-add-btn')

    # order element creation
    ORDER_ELEM_TYPE_INPUT = (By.CSS_SELECTOR, '#order-elem-type-input input')
    ORDER_ELEM_PRODUCT_INPUT = (By.CSS_SELECTOR, '#order-elem-product-input input')
    ORDER_ELEM_COUNT_INPUT = (By.CSS_SELECTOR, '#order-elem-count-input input')
    ORDER_ELEM_ACCOUNT_INPUT = (By.CSS_SELECTOR, '#order-elem-account-input input')
    ORDER_ELEM_MVZ_INPUT = (By.CSS_SELECTOR, '#order-elem-mvz-input input')
    ORDER_ELEM_INNER_INPUT = (By.CSS_SELECTOR, '#order-elem-inner-input input')
    ORDER_ELEM_PRICE_INPUT = (By.CSS_SELECTOR, '#order-elem-price-input input')
    ORDER_ELEM_STORAGE_INPUT = (By.CSS_SELECTOR, '#order-elem-storage-input input')
    ORDER_ELEM_ROW_INPUT = (By.CSS_SELECTOR, '#order-elem-row-input input')
    ORDER_ELEM_STACK_INPUT = (By.CSS_SELECTOR, '#order-elem-stack-input input')
    ORDER_ELEM_BOARD_INPUT = (By.CSS_SELECTOR, '#order-elem-board-input input')
    ORDER_ELEM_CELL_INPUT = (By.CSS_SELECTOR, '#order-elem-cell-input input')
    ORDER_ELEM_SAVE_BTN = (By.ID, 'order-elem-save-btn')

    # order element info
    ORDER_ELEM_INFO_TYPE = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[2]//span/span')
    ORDER_ELEM_INFO_ACCOUNT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[3]//span/span')
    ORDER_ELEM_INFO_MVZ = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[4]//span/span')
    ORDER_ELEM_INFO_INNER = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[5]//span/span')
    ORDER_ELEM_INFO_PRODUCT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[6]//span/span')
    ORDER_ELEM_INFO_COUNT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[7]//span/span')
    ORDER_ELEM_INFO_NETTO = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[8]//span/span')
    ORDER_ELEM_INFO_PRICE = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[9]//span/span')
    ORDER_ELEM_INFO_UNIT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[10]//span/span')
    ORDER_DRAFT_DELETE_ELEM_BTN = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[11]/div/div')


class DeliveryPageLocators:
    CREATE_DELIVERY_BTN = (By.ID, 'delivery-create-btn')

    # delivery creation
    DELIVERY_DATE_INPUT = (By.CSS_SELECTOR, '#delivery-date-input input')
    DELIVERY_DATE_INPUT_LABEL = (By.CSS_SELECTOR, '#delivery-date-input label')

    DELIVERY_RESPONSIBLE_INPUT = (By.CSS_SELECTOR, "#delivery-responsible-input input")
    DELIVERY_SAVE_BTN = (By.ID, 'delivery-save-btn')

    # delivery draft
    DELIVERY_DRAFT_DATE_INPUT = (By.CSS_SELECTOR, '#delivery-draft-date-input input')
    DELIVERY_DRAFT_RESPONSIBLE_INPUT = (By.CSS_SELECTOR, '#delivery-draft-responsible-input input')
    DELIVERY_DRAFT_SAVE_BTN = (By.ID, 'delivery-draft-save-btn')
    DELIVERY_DRAFT_ADD_BTN = (By.ID, 'delivery-draft-add-btn')

    # delivery info
    DELIVERY_INFO_DATE = (By.XPATH, '//tbody/tr[1]/td[2]//span/span')
    DELIVERY_INFO_RESPONSIBLE = (By.XPATH, '//tbody/tr[1]/td[3]//span/span')
    DELIVERY_DELETE_BTN = (By.XPATH, '//tbody/tr[1]/td[4]/div[@class="cell"]')

    # delivery element creation
    DELIVERY_ELEM_PRODUCT_INPUT = (By.CSS_SELECTOR, '#delivery-elem-product-input input')
    DELIVERY_ELEM_COUNT_INPUT = (By.CSS_SELECTOR, '#delivery-elem-count-input input')
    DELIVERY_ELEM_STORAGE_INPUT = (By.CSS_SELECTOR, '#delivery-elem-storage-input input')
    DELIVERY_ELEM_ROW_INPUT = (By.CSS_SELECTOR, '#delivery-elem-row-input input')
    DELIVERY_ELEM_STACK_INPUT = (By.CSS_SELECTOR, '#delivery-elem-stack-input input')
    DELIVERY_ELEM_BOARD_INPUT = (By.CSS_SELECTOR, '#delivery-elem-board-input input')
    DELIVERY_ELEM_CELL_INPUT = (By.CSS_SELECTOR, '#delivery-elem-cell-input input')
    DELIVERY_ELEM_SAVE_BTN = (By.ID, 'delivery-elem-save-btn')

    # delivery element info
    DELIVERY_ELEM_INFO_PRODUCT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[2]//span/span')
    DELIVERY_ELEM_INFO_COUNT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[3]//span/span')
    DELIVERY_ELEM_INFO_STORAGE = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[4]//span/span')
    DELIVERY_ELEM_INFO_ROW = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[5]//span/span')
    DELIVERY_ELEM_INFO_STACK = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[6]//span/span')
    DELIVERY_ELEM_INFO_BOARD = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[7]//span/span')
    DELIVERY_ELEM_INFO_CELL = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[8]//span/span')
    DELIVERY_DRAFT_DELETE_ELEM_BTN = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[9]/div/div')
