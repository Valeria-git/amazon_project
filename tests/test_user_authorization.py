import sys
sys.path.append("/Users/your_name/Desktop/amazon_project")
from pages.login_page import LoginPage
import pytest
import allure





allure.description("Authorization")
def test_authorization(set_up):

        login = LoginPage(set_up)
        login.authorization()
        assert login.get_basket_lable().is_displayed(), "Authorization failed"


