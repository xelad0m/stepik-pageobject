from pages.main_page import MainPage

LINK = "http://selenium1py.pythonanywhere.com/"
# LINK = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
LOGIN = "http://selenium1py.pythonanywhere.com/accounts/login/"

def test_guest_can_go_to_login_page(browser):
    link = LINK
    page = MainPage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page()          # выполняем метод страницы — переходим на страницу логина

def test_guest_should_see_login_link(browser):
    link = LINK
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()