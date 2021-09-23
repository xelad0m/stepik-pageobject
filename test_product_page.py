import pytest
from pages.product_page import ProductPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{n}" for n in range(10)]

xfails = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", ]
marked_urls = [url if url not in xfails else pytest.param(url, marks=pytest.mark.xfail) for url in urls]


@pytest.mark.parametrize('link', marked_urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()git 