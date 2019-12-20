from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_add_to_basket_btn(self):
        assert self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN), "There is no add to basket form"

    def add_product_to_basket(self):
        add_to_basket_form = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_form.click()

    def should_be_product_in_basket(self):
        self.should_be_message_about_adding_product()
        self.should_be_message_about_basket_total()

    def should_be_message_about_adding_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME), (
            "Product name is not presented")
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING), (
            "Message about adding is not presented")
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        message_about_adding = self.browser.find_element(*ProductPageLocators.MESSAGE_ABOUT_ADDING).text
        assert product_name == message_about_adding, "Product name is not presented in message about adding"

    def should_be_message_about_basket_total(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE), (
            "Product price is not presented")
        assert self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL), (
            "Basket total message is not presented")
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_total_message = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_TOTAL).text
        assert product_price == basket_total_message, "Basket total message is not equal product price"
