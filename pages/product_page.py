from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base
from logger import Logger
import allure



class ProductPage(Base):

    

    #Locators

    radio_button_buy_without_free_trial = "(//div[@data-test='adbl_bb_header_text'])[2]"
    add_to_cart_button = "//input[@type='submit' and @aria-labelledby=//span[normalize-space(.)='Add to Cart']/@id]"
    added_to_cart_label = "//h1[@class='a-size-medium-plus a-color-base sw-atc-text a-text-bold']"


    #Getters

    def get_radio_button_buy_without_free_trial(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.radio_button_buy_without_free_trial)))
    
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_added_to_cart_label(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.added_to_cart_label)))
    
    
   
    #Actions
    def click_radio_button_buy_without_free_trial(self):
        element = self.get_radio_button_buy_without_free_trial()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        print("click_radio_button_buy_without_free_trial")

    def click_add_to_cart_button(self):
        element = self.get_add_to_cart_button()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        print("click_add_to_cart_button")

    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

 

 
    """Adding book to cart"""
    def buy_book(self):
        with allure.step("Add product to cart"):
            Logger.add_start_step(method = "buy_book")

            self.get_current_url()


            self.click_radio_button_buy_without_free_trial()
            self.click_add_to_cart_button()
            self.assert_word(self.get_added_to_cart_label(), "Added to cart")


            self.get_screenshot()
            Logger.add_end_step(url = self.driver.current_url, method = "buy_book")


 