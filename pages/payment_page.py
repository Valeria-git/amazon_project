from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base


class PaymentPage(Base):

    

    #Locators

    payment_label = "//div[@class='a-column a-span8 a-spacing-base']/h2"





    #Getters

    def get_payment_lable(self):
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, self.payment_label)))
    
    



    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

 

 

    def payment(self):

        self.get_current_url()

        self.assert_word(self.get_payment_lable(), 'Payment method')
        self.get_screenshot()
 