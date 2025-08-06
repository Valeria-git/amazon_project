from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base
import json
import os

class LoginPage(Base):


    #Locators
    user_name = "//input[@id='ap_email']"
    continue_button = "//input[@id='continue']"
    password = "//input[@id='ap_password']"
    sign_in_button = "//input[@id='signInSubmit']"
    basket_lable = "//span[@class='nav-cart-icon nav-sprite']"

    



    #Getters

    def get_user_name(self):
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, self.user_name)))
 
    def get_password(self):
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, self.password)))
    
    def get_continue_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))


    def get_sign_in_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.sign_in_button)))
    
    def get_basket_lable(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.basket_lable)))


    #Actions

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input user name")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Click continue button")

    def click_sign_in_button(self):
        self.get_sign_in_button().click()
        print("Click sign in button")
    

    



    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

 

 
    """Login"""
    def authorization(self):


        self.get_current_url()

        json_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "utils", "credentials.json")
        with open(json_path) as f:
            creds = json.load(f)


        self.input_user_name(creds["email"])
        self.click_continue_button()
        self.input_password(creds["password"])
        self.click_sign_in_button()

 