from time import sleep
import pytest

from pages.locators import ItemPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=20)
    page.open()
    page.add_to_basket()
    page.look_for_item_in_basket_message()
    page.is_basket_price_valid()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_to_basket()
    page.success_message_is_not_present()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.success_message_is_not_present()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_to_basket()
    page.success_message_is_not_present()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    cur_link = browser.current_url
    page = BasketPage(browser, cur_link)
    page.basket_should_be_empty()
    page.should_be_basket_is_empty_text()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self, browser):
        init_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, init_link)
        page.open()
        email = page.generate_email()
        page.register_new_user(email, 'Password12345.')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link, timeout=20)
        page.open()
        page.add_to_basket()
        page.look_for_item_in_basket_message()
        page.is_basket_price_valid()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link, timeout=0)
        page.open()
        page.success_message_is_not_present()
