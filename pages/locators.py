from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')
    EMAIL_FIELD = (By.CSS_SELECTOR, '#id_registration-email')
    PASSWORD_FIELD = (By.CSS_SELECTOR, '#id_registration-password1')
    PASSWORD_CONFIRMATION_FIELD = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')

class ItemPageLocators:
    ADDTOBASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_PRICE = (By.CSS_SELECTOR, '.price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '.btn-cart')
    ITEM_NAME = (By.CSS_SELECTOR, '.row .col-sm-6.product_main h1')
    ADDED_TO_BASKET_NAME = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages :nth-child(1).alert-success')

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//a[text()="View basket"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, '.page_inner .content p')
    BASKET_ITEMS = (By.CSS_SELECTOR, '.basket-items')
