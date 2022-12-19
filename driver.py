from selenium import webdriver


class Driver:
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--start-maximized")
        self.options.add_argument("--lang=en")
        self.driver = webdriver.Chrome()

    def start_chrome_driver(self):
        self.driver = webdriver.Chrome()
        return self.driver

    def get_current_url(self):
        return self.driver.current_url

    def close_driver(self):
        self.driver.close()
