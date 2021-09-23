from .base_page import BasePage
from .locators import ProductPageLocators

import time

class ProductPage(BasePage):  
    def _get_title(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
    
    def _get_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_to_basket(self):
        title = self._get_title()
        price = self._get_price()

        button = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        button.click()

        self.solve_quiz_and_get_code()
        
        msg_title, _, msg_price = (msg.text for msg in self.browser.find_elements(*ProductPageLocators.MESSAGES))
        print(f"{title=}, {price=}")
        print(f"{msg_title=}, {msg_price=}")

        self.sould_be_correct_title(msg_title, title)
        self.sould_be_correct_price(msg_price, price)

    def sould_be_correct_title(self, msg_title, title):
        assert msg_title == title, f"'{title}' added, but '{msg_title}' in basket"
    
    def sould_be_correct_price(self, msg_price, price):
        assert msg_price == price, f"'{price}' price added, but '{msg_price}' in basket"

    def should_be_success_message(self):
        assert not self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is NOT presented"
    
    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should NOT be"
    
    def should_disapear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is NOT desapeaded, but should be"