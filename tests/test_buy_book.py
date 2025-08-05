import sys
sys.path.append("/Users/your_name/Desktop/amazon_project")
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.payment_page import PaymentPage
import pytest



def test_buy_book(set_up):


        login = LoginPage(set_up)
        login.authorization()
        assert login.get_basket_lable().is_displayed(), "Authorization failed"

        main = MainPage(set_up)
        main.find_book()

        product = ProductPage(set_up)
        product.buy_book()

        basket = BasketPage(set_up)
        basket.checkout()

        payment = PaymentPage(set_up)
        payment.payment()




