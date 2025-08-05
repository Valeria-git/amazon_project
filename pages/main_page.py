from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from base.base import Base


class MainPage(Base):

    

    #Locators
    burger_menu = "//span[@class='hm-icon-label']"
    audible_books_and_originals_link = "//a[@data-menu-id='9']"
    audible_books_and_originals_link_submenu = "//*[@id='hmenu-content']/div[9]/section/ul/li[2]/a"


    romance_type = "(//li[@class='a-spacing-micro apb-browse-refinements-indent-2'])[19]"
    historical_romance_type = "(//span[@class='a-size-base a-color-base'])[10]"
    duration = "//li[@id='p_n_feature_seven_browse-bin/18685633011']"
    language = "//li[@id='p_n_feature_six_browse-bin/18685580011']"
    first_book = "((//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal'])[1]/ancestor::a)[1]"

    
    



    #Getters

    def get_burger_menu(self):
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, self.burger_menu)))
 
    def get_audible_books_and_originals_link(self):
        return WebDriverWait(self.driver, 6).until(EC.visibility_of_element_located((By.XPATH, self.audible_books_and_originals_link)))
    
    def get_audible_books_and_originals_link_submenu(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.audible_books_and_originals_link_submenu)))


    def get_romance_type(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.romance_type)))
    
    def get_historical_romance_type(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.historical_romance_type)))

    def get_duration(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.duration)))
    
    def get_language(self):
        return WebDriverWait(self.driver, 6).until(EC.element_to_be_clickable((By.XPATH, self.language)))
    
    def get_first_book(self):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, self.first_book)))
    
    

    #Actions

    def click_burger_menu(self):
        self.get_burger_menu().click()
        print("Click burger menu link")

    def click_audible_books_and_originals_link(self):
        self.get_audible_books_and_originals_link().click()
        print("Click audible books and originalslink")


    def click_audible_books_and_originals_link_submenu(self):
        element = self.get_audible_books_and_originals_link_submenu()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)
        print("Click Aaudible books and riginals link submenu")


    def click_romance_type(self):
        self.get_romance_type().click()
        print("Click romance type")
    
    def click_historical_romance_type(self):
        self.get_historical_romance_type().click()
        print("Click historical romance type")
    
    def click_get_duration(self):
        self.get_duration().click()
        print("Click get duration")

    def click_language(self):
        self.get_language().click()
        print("Click language")


    def click_first_book(self):
        element = self.get_first_book()
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        self.driver.execute_script("arguments[0].click();", element)

        print("The book selected")


    def __init__(self, driver):
        super().__init__(driver=driver)
        self.driver = driver

 

 

    def find_book(self):

        self.get_current_url()


        self.click_burger_menu()
        self.click_audible_books_and_originals_link()
        self.click_audible_books_and_originals_link_submenu()
        self.click_romance_type()
        self.click_historical_romance_type()
        self.click_get_duration()
        self.click_language()
        self.click_first_book()

        
        self.get_screenshot()
 