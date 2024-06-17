from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators

def test_this_is_promo_url(browser):
    link = (ProductPageLocators.PRODUCT_PAGE)
    page = ProductPage(browser, link)
    page.open()
    page.should_to_go_promo_product_link()

def test_guest_can_see_button(browser):
    link = (ProductPageLocators.PRODUCT_PAGE)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_basket_btn()

def test_guest_click_to_button(browser):
    link = (ProductPageLocators.PRODUCT_PAGE)
    page = ProductPage(browser, link)
    page.open()
    page.btn_should_be_clickable()
    page.solve_quiz_and_get_code()
    page.message_about_product()
    page.total_price()
