import sys
sys.path.append("/Users/your_name/Desktop/amazon_project")
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.payment_page import PaymentPage
import pytest




def test_delete_product_from_cart(set_up):
        login = LoginPage(set_up)
        login.authorization()
        assert login.get_basket_lable().is_displayed(), "Authorization failed"

        basket = BasketPage(set_up)
        basket.delete_product_from_basket()


