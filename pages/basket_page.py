from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base
from selenium.common.exceptions import TimeoutException

class BasketPage(Base):

    

    #Locators

    proceed_to_check_out_button = "//input[@data-feature-id='proceed-to-checkout-action']"
    delete_from_basket_button = "//input[@data-action='delete-active']"
    empty_cart_label = "//h3[@class='a-size-large a-spacing-top-base sc-your-amazon-cart-is-empty']"
    not_empty_cart_label = "//*[@id='sc-active-cart']/div/div/div[1]"
    basket_button = "//div[@id='nav-cart-count-container']"


    

    #Getters

    def get_proceed_to_check_out_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.proceed_to_check_out_button)))
    
    def get_delete_from_basket_button(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.delete_from_basket_button)))


    def get_empty_cart_label(self):
        try:
            return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.empty_cart_label)))
        except TimeoutException:
             return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.not_empty_cart_label)))
    
    def get_basket_button(self):
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, self.basket_button)))
 

    
    #Actions

    def click_proceed_to_check_out_button(self):
        self.get_proceed_to_check_out_button().click()
        print("Proceed to check out")

    def click_delete_from_basket_button(self):
        self.get_delete_from_basket_button().click()
        print("Click delete form basket")

    def click_basket_button(self):
        self.get_basket_button().click()
        print("Click basket button")



    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

 

 

    def checkout(self):

        self.get_current_url()
        self.click_basket_button()
        self.assert_url("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
        self.click_proceed_to_check_out_button()

        self.get_screenshot()
 

    def delete_product_from_basket(self):
        self.get_current_url()
        self.click_basket_button()
        self.assert_url("https://www.amazon.com/gp/cart/view.html?ref_=nav_cart")
        if self.is_word_present(self.get_empty_cart_label(), "Your Amazon Cart is empty"):
            print("Basket empty")
        else:
            self.click_delete_from_basket_button()
        self.get_screenshot()
