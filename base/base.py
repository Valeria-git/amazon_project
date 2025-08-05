import datetime
import os


class Base:




    def __init__(self, driver):
        self.driver = driver


    """Method get current url"""
    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)


    """Method assert word"""

    def assert_word(self, actual_result, expected_result):
        value_actual_result = actual_result.text
        assert value_actual_result == expected_result
        print("Word presentense check passed")

    def is_word_present(self, actual_result, expected_result):
        return actual_result.text == expected_result



    def assert_url(self, expected_result):
        get_url = self.driver.current_url
        assert get_url == expected_result
        print("URL check passed")


    """Method scrinshot"""
    def get_screenshot(self):
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        screen_dir = os.path.join(base_dir, "screen")
        os.makedirs(screen_dir, exist_ok=True)
    
        now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screen = "amazon_screen"
    
        screenshot_path = os.path.join(screen_dir, f"{name_screen}_{now_date}.png")
        self.driver.save_screenshot(screenshot_path)

    