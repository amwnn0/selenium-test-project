import pytest

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.basket_page import BasketPage
from pages.product_page import ProductPage


@pytest.mark.login_guest
class TestLoginFromMainPage:
    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser,
                        link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.negative
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_basket_link()
    page.go_to_basket_page()
    link = browser.current_url
    page = BasketPage(browser, link)
    page.basket_should_be_empty()
    page.should_be_basket_is_empty_text()
