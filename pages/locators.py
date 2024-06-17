from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = ("https://selenium1py.pythonanywhere.com/ru/accounts/login")
    LOGIN_FORM = (By.CSS_SELECTOR, "[name='login-username']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "[name='registration-email']")

class ProductPageLocators():
    PRODUCT_PAGE = ("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
    PRODUCT_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    MESSAGE_SUCCESS_ADDING = (By.CSS_SELECTOR, "div.alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_IN_BASKET = (By.CSS_SELECTOR, ".alert-info .alertinner strong")

