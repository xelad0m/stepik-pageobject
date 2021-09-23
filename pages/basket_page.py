from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_empty(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE),\
            "Empty basket message not found, but it should be"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCT_LIST),\
            "List of products found, but it should not"