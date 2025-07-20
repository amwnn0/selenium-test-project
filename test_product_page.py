from time import sleep
import pytest

from pages.locators import ItemPageLocators
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage

# n = (0-9), 7 xfail
urls = [f'?promo=offer{n}' if n!=7 else pytest.param(7, marks=pytest.mark.xfail) for n in range(10)]

@pytest.mark.need_review
@pytest.mark.parametrize('url', urls)
def test_guest_can_add_product_to_basket(browser, url):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/' + url
    page = ProductPage(browser, link, timeout=20)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.look_for_item_in_basket_message()
    page.is_basket_price_valid()


link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'

@pytest.mark.skip
@pytest.mark.negative
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE), "Success message should not be present after adding to basket."

@pytest.mark.negative
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    assert page.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE), "Success message should not be present."

@pytest.mark.skip
@pytest.mark.negative
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link, timeout=0)
    page.open()
    page.add_to_basket()
    assert page.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE), "Success message must disappear."

@pytest.mark.login
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
@pytest.mark.login
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    assert '/login' in page.browser.current_url, 'Login page should be opened.'

@pytest.mark.need_review
@pytest.mark.negative
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    link = browser.current_url
    page = BasketPage(browser, link)
    page.basket_should_be_empty()
    page.should_be_basket_is_empty_text()

@pytest.mark.register_user
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True, scope='function')
    def setup(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, link)
        page.open()
        email = page.generate_email()
        page.register_new_user(email, 'Password12345.')
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link, timeout=20)
        page.open()
        page.add_to_basket()
        page.look_for_item_in_basket_message()
        page.is_basket_price_valid()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link, timeout=0)
        page.open()
        assert page.is_not_element_present(*ItemPageLocators.SUCCESS_MESSAGE), "Success message should not be present."
