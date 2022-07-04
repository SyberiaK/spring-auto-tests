from selenium.webdriver.common.by import By


class BasePageLocators:
    """LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a.btn")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")"""


class WorkPageLocators:
    MSGBOX_CANCEL_BTN = (By.CSS_SELECTOR, '.msgbox-cancel-btn')
    MSGBOX_LEAVE_BTN = (By.CSS_SELECTOR, '.msgbox-leave-btn')
    MSGBOX_CANCEL_ELEM_BTN = (By.CSS_SELECTOR, '.el-button--default.el-button--small')
    MSGBOX_DELETE_ELEM_BTN = (By.CSS_SELECTOR, '.el-button--small.is-plain')


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
    # ORDER_SHOP_DROPDOWN = (By.ID, 'order-shop-dropdown')
    # ORDER_SHOP_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-shop-dropdown li')
    # ORDER_SHOP_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-shop-dropdown li > span')

    ORDER_PROVIDER_INPUT = (By.CSS_SELECTOR, '#order-provider-input input')
    # ORDER_PROVIDER_DROPDOWN = (By.ID, 'order-provider-dropdown')
    # ORDER_PROVIDER_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-provider-dropdown li')
    # ORDER_PROVIDER_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-provider-dropdown li > span')

    ORDER_SAVE_BTN = (By.ID, 'order-save-btn')
    ORDER_CLOSE_BTN = (By.CSS_SELECTOR, 'button.el-dialog__headerbtn')

    # order info
    ORDER_INFO = (By.CSS_SELECTOR, 'tbody tr')
    ORDER_INFO_NUMBER = (By.XPATH, '//tbody/tr[1]/td[1]//span/span')
    ORDER_INFO_DATE = (By.XPATH, '//tbody/tr[1]/td[2]//span/span')
    ORDER_INFO_PROVIDER = (By.XPATH, '//tbody/tr[1]/td[3]//span/span')
    ORDER_INFO_NETTO = (By.XPATH, '//tbody/tr[1]/td[4]//span/span')
    ORDER_INFO_STATUS = (By.XPATH, '//tbody/tr[1]/td[5]//span/span')

    # order draft
    ORDER_DRAFT_NUMBER_INPUT = (By.CSS_SELECTOR, '#order-draft-number-input input')
    ORDER_DRAFT_DATE_INPUT = (By.CSS_SELECTOR, '#order-draft-date-input input')

    ORDER_DRAFT_SHOP_INPUT = (By.CSS_SELECTOR, '#order-draft-shop-input input')
    # ORDER_DRAFT_SHOP_DROPDOWN = (By.ID, 'order-draft-shop-dropdown')
    # ORDER_DRAFT_SHOP_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-draft-shop-dropdown li')
    # ORDER_DRAFT_SHOP_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-draft-shop-dropdown li > span')

    ORDER_DRAFT_PROVIDER_INPUT = (By.CSS_SELECTOR, '#order-draft-provider-input input')
    # ORDER_DRAFT_PROVIDER_DROPDOWN = (By.ID, 'order-provider-dropdown')
    # ORDER_DRAFT_PROVIDER_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-provider-dropdown li')
    # ORDER_DRAFT_PROVIDER_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-provider-dropdown li > span')

    ORDER_DRAFT_DOWNLOAD_BTN = (By.ID, 'order-draft-download-btn')
    ORDER_DRAFT_CANCEL_BTN = (By.ID, 'order-draft-cancel-btn')
    ORDER_DRAFT_FINISH_BTN = (By.ID, 'order-draft-finish-btn')
    ORDER_DRAFT_SAVE_BTN = (By.ID, 'order-draft-save-btn')
    ORDER_DRAFT_ADD_BTN = (By.ID, 'order-draft-add-btn')
    ORDER_DRAFT_DELETE_ELEM_BTN = (By.XPATH, '//tbody/tr[1]/td[11]/div/div')

    # order element creation
    ORDER_ELEM_TYPE_INPUT = (By.CSS_SELECTOR, '#order-elem-type-input input')
    # ORDER_ELEM_TYPE_DROPDOWN = (By.ID, 'order-elem-type-dropdown')
    # ORDER_ELEM_TYPE_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-type-dropdown li')
    # ORDER_ELEM_TYPE_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-type-dropdown li > span')

    ORDER_ELEM_PRODUCT_INPUT = (By.CSS_SELECTOR, '#order-elem-product-input input')
    # ORDER_ELEM_PRODUCT_DROPDOWN = (By.ID, 'order-elem-product-dropdown')
    # ORDER_ELEM_PRODUCT_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-product-dropdown li')
    # ORDER_ELEM_PRODUCT_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-product-dropdown li > span')

    ORDER_ELEM_COUNT_INPUT = (By.CSS_SELECTOR, '#order-elem-count-input input')

    ORDER_ELEM_ACCOUNT_INPUT = (By.CSS_SELECTOR, '#order-elem-account-input input')
    # ORDER_ELEM_ACCOUNT_DROPDOWN = (By.ID, 'order-elem-account-dropdown')
    # ORDER_ELEM_ACCOUNT_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-account-dropdown li')
    # ORDER_ELEM_ACCOUNT_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-account-dropdown li > span')

    ORDER_ELEM_MVZ_INPUT = (By.CSS_SELECTOR, '#order-elem-mvz-input input')
    # ORDER_ELEM_MVZ_DROPDOWN = (By.ID, 'order-elem-mvz-dropdown')
    # ORDER_ELEM_MVZ_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-mvz-dropdown li')
    # ORDER_ELEM_MVZ_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-mvz-dropdown li > span')

    ORDER_ELEM_INNER_INPUT = (By.CSS_SELECTOR, '#order-elem-inner-input input')
    # ORDER_ELEM_INNER_DROPDOWN = (By.ID, 'order-elem-inner-dropdown')
    # ORDER_ELEM_INNER_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-inner-dropdown li')
    # ORDER_ELEM_INNER_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-inner-dropdown li > span')

    ORDER_ELEM_PRICE_INPUT = (By.CSS_SELECTOR, '#order-elem-price-input input')

    ORDER_ELEM_STORAGE_INPUT = (By.CSS_SELECTOR, '#order-elem-storage-input input')
    # ORDER_ELEM_STORAGE_DROPDOWN = (By.ID, 'order-elem-storage-dropdown')
    # ORDER_ELEM_STORAGE_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-storage-dropdown li')
    # ORDER_ELEM_STORAGE_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-storage-dropdown li > span')

    ORDER_ELEM_ROW_INPUT = (By.CSS_SELECTOR, '#order-elem-row-input input')
    # ORDER_ELEM_ROW_DROPDOWN = (By.ID, 'order-elem-row-dropdown')
    # ORDER_ELEM_ROW_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-row-dropdown li')
    # ORDER_ELEM_ROW_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-row-dropdown li > span')

    ORDER_ELEM_STACK_INPUT = (By.CSS_SELECTOR, '#order-elem-stack-input input')
    # ORDER_ELEM_STACK_DROPDOWN = (By.ID, 'order-elem-stack-dropdown')
    # ORDER_ELEM_STACK_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-stack-dropdown li')
    # ORDER_ELEM_STACK_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-stack-dropdown li > span')

    ORDER_ELEM_BOARD_INPUT = (By.CSS_SELECTOR, '#order-elem-board-input input')
    # ORDER_ELEM_BOARD_DROPDOWN = (By.ID, 'order-elem-board-dropdown')
    # ORDER_ELEM_BOARD_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-board-dropdown li')
    # ORDER_ELEM_BOARD_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-board-dropdown li > span')

    ORDER_ELEM_CELL_INPUT = (By.CSS_SELECTOR, '#order-elem-cell-input input')
    # ORDER_ELEM_CELL_DROPDOWN = (By.ID, 'order-elem-cell-dropdown')
    # ORDER_ELEM_CELL_DROPDOWN_CONTENT = (By.CSS_SELECTOR, '#order-elem-cell-dropdown li')
    # ORDER_ELEM_CELL_DROPDOWN_CONTENT_SPAN = (By.CSS_SELECTOR, '#order-elem-cell-dropdown li > span')

    ORDER_ELEM_SAVE_BTN = (By.ID, 'order-elem-save-btn')
    ORDER_ELEM_CLOSE_BTN = (By.CSS_SELECTOR, 'button.el-dialog__headerbtn')

    # order element info
    ORDER_ELEM_INFO = (By.CSS_SELECTOR, 'div.AppTable tbody tr')
    ORDER_ELEM_INFO_TYPE = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[2]//span/span')
    ORDER_ELEM_INFO_ACCOUNT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[3]//span/span')
    ORDER_ELEM_INFO_MVZ = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[4]//span/span')
    ORDER_ELEM_INFO_INNER = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[5]//span/span')
    ORDER_ELEM_INFO_PRODUCT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[6]//span/span')
    ORDER_ELEM_INFO_COUNT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[7]//span/span')
    ORDER_ELEM_INFO_NETTO = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[8]//span/span')
    ORDER_ELEM_INFO_PRICE = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[9]//span/span')
    ORDER_ELEM_INFO_UNIT = (By.XPATH, '//div[@class="AppTable"]//tbody/tr[1]/td[10]//span/span')

    DROPDOWN_CONTENT = (By.XPATH, '//div[@aria-hidden="false"]//li')
    DROPDOWN_CONTENT_SPAN = (By.XPATH, '//div[@aria-hidden="false"]//li/span')  # для некоторых полей
