from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url,\
            "Current URL does not contain 'login' substring"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM),\
            "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM),\
            "Register form is not presented"

    def register_new_user(self, email, password):
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        pwd1_field = self.browser.find_element(*LoginPageLocators.PWD1_FIELD)
        pwd1_field.send_keys(password)
        pwd2_field = self.browser.find_element(*LoginPageLocators.PWD2_FIELD)
        pwd2_field.send_keys(password)

        btn = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        btn.click()

        # self.should_be_registred()
    
    def should_be_registred(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_OK),\
            "Registeration confirmation was not recived"


