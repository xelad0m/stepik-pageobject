import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage

product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{n}" for n in range(10)]

xfails = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", ]
marked_urls = [url if url not in xfails else pytest.param(url, marks=pytest.mark.xfail) for url in urls]


@pytest.mark.parametrize('link', marked_urls)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()


@pytest.mark.xfail(reason="guest must see succes message")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = marked_urls[0]
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = marked_urls[0]
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="succes message has no disapear behavoir")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = marked_urls[0]
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_disapear_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()       # выполнение тестов на странице логина