from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def should_to_go_promo_product_link(self):
        assert "newYear" in (ProductPageLocators.PRODUCT_PAGE), "Wrong URL" #Проверяем URL
    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_BUTTON), "Button 'Add to basket' not available"
#Проверяем кнопку, на момент написания тестов, кнопки не было"
    def btn_should_be_clickable(self):
        button1 = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON)
        button1.click()
#Все в наличии жмём на кнопку
    def message_about_product(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product not found"
        assert self.is_element_present(*ProductPageLocators.MESSAGE_SUCCESS_ADDING), "Message not found"
        message_basket = self.browser.find_element(*ProductPageLocators.MESSAGE_SUCCESS_ADDING).text
        name_of_product = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert name_of_product in message_basket, "Product not in basket"

    def total_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Not found product price"
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_BASKET), "Product not in basket"
        price_product = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        basket_price = self.browser.find_element(*ProductPageLocators.PRICE_IN_BASKET).text
        assert price_product == basket_price, "Product not in basket"