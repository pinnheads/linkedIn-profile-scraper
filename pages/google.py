from selenium.webdriver.common.by import By


class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = "//input[@title='Search']"
        self.captcha = "//*[contains(@id, 'recaptcha')]"
        self.result_title = "//h3"
        self.result_link = "//h3/parent::a"
        self.next = "//span[contains(text(), 'Next')]/parent::a"

    def search_input_element(self):
        """
        Returns the search input element from www.google.com
        """
        return self.driver.find_element(By.XPATH, self.search_input)

    def captcha_element(self):
        """
        Returns the captcha element
        """
        return self.driver.find_element(By.XPATH, self.captcha)

    def result_title_list(self):
        """
        Returns the list of titles from a google search page
        """
        return self.driver.find_elements(By.XPATH, self.result_title)

    def result_link_list(self):
        """
        Returns the list of links from a google search page
        """
        return self.driver.find_elements(By.XPATH, self.result_link)

    def next_button(self):
        """
        Returns the next button from the google search page
        """
        return self.driver.find_element(By.XPATH, self.next)
