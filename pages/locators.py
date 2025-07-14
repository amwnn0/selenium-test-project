from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')

class ItemPageLocators:
    ADDTOBASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    ITEM_PRICE = (By.CSS_SELECTOR, '.price_color')
    BASKET_PRICE = (By.CSS_SELECTOR, '.btn-cart')
    ITEM_NAME = (By.CSS_SELECTOR, '.product_main h1')
    ADDED_TO_BASKET_NAME = (By.CSS_SELECTOR, '#messages :nth-child(1) .alertinner strong')