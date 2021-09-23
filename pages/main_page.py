from .base_page import BasePage

from .locators import MainPageLocators

from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def __init__(self, *args, **kwargs):
        """
        пока специфических методов нет, а страница логина доступна на 
        всех страницах, поэтому переход на нее перенесен в BasePage
        """
        super(MainPage, self).__init__(*args, **kwargs)


    