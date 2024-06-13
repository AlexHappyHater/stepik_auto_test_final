from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = ("https://selenium1py.pythonanywhere.com/ru/accounts/login")
    LOGIN_FORM = (By.CSS_SELECTOR, "[name='login-username']")
    REGISTRATION_FORM = (By.CSS_SELECTOR, "[name='registration-email']")

class ProductPage():
    PRODUCT_PAGE = ("http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear")
    PRODUCT_BUTTON = (By.CSS_SELECTOR, "[class='btn btn-lg btn-info btn-add-to-basket']")
