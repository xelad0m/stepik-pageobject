import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

LINK = "http://selenium1py.pythonanywhere.com/"
# LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_should_see_login_link(self, browser):
        link = LINK
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        link = LINK
        page = MainPage(browser, link)          # передаем в конструктор экземпляр драйвера и url адрес 
        page.open() 

        # вариант с инициализацией новой страницы в MainPage (типа неявный переход)
        # login_page = page.go_to_login_page()    # переход на страницу логина

        # вариант с инициализацией объекта страницы в теле теста
        # (меньше рисков перекрестного импорта при усложнении тестов)
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)

        login_page.should_be_login_page()       # выполнение тестов на странице логина


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = LINK
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_empty()
