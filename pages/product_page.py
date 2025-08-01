from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage
from .locators import ItemPageLocators
from selenium.common.exceptions import NoAlertPresentException, NoSuchElementException
from math import sin, log


class ProductPage(BasePage):
    def add_to_basket(self):
        try:
            button = self.browser.find_element(*ItemPageLocators.ADDTOBASKET_BUTTON)
            button.click()
        except NoSuchElementException:
            print('Add to basket button should be present')

    def solve_quiz_and_get_code(self):
        WebDriverWait(self.browser, 10).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(' ')[2]
        answer = str(log(abs((12 * sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f'Your code: {alert_text}')
            alert.accept()
        except NoAlertPresentException:
            print('No second alert present')

    def look_for_item_in_basket_message(self):
        item_name = self.browser.find_element(*ItemPageLocators.ITEM_NAME).text
        added_to_basket_name = self.browser.find_element(*ItemPageLocators.ADDED_TO_BASKET_NAME).text
        assert item_name == added_to_basket_name, 'Appearing message should contain same item name'

    def is_basket_price_valid(self):
        item_price = self.browser.find_element(*ItemPageLocators.ITEM_PRICE).text
        basket_price = self.browser.find_element(*ItemPageLocators.BASKET_PRICE).text
        assert item_price == basket_price, 'Basket price does not match item price'

    def success_message_is_not_present(self):
        assert self.browser.is_not_element_present(
            *ItemPageLocators.SUCCESS_MESSAGE), "Success message should not be present"
