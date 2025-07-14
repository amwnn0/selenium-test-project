from time import sleep
import pytest
from pages.product_page import ItemPage

# n = (0-9), 7 xfail
urls = [f'?promo=offer{n}' if n!=7 else pytest.param(7, marks=pytest.mark.xfail) for n in range(10)]

@pytest.mark.parametrize('url', urls)
def test_guest_can_add_product_to_basket(browser, url):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/' + url
    page = ItemPage(browser, link, timeout=20)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.look_for_item_in_basket_message()
    page.is_basket_price_valid()