from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

company_name = input("Enter a company name: ")
job_title = input("Enter job title: ")

driver = webdriver.Chrome()

driver.get("https://www.google.com")
sleep(3)

search_input = driver.find_element(By.XPATH, "//input[@title='Search']")
search_input.send_keys(
    f"site:in.linkedin.com/in intitle:{job_title} {company_name}", Keys.ENTER
)
try:
    captcha = driver.find_element(By.XPATH, "//*[contains(@id, 'recaptcha')]")
    if captcha.is_displayed():
        sleep(120)
except:
    print("captcha not displayed")
next_btn_displayed = True
while next_btn_displayed:
    titles = driver.find_elements(By.XPATH, "//h3")
    links = driver.find_elements(By.XPATH, "//h3/parent::a")
    for (title, link) in zip(titles, links):
        print(title.text)
        print(link.get_attribute("href"))
    try:
        next_button = driver.find_element(
            By.XPATH, "//span[contains(text(), 'Next')]/parent::a"
        )
        next_button.click()
    except:
        next_btn_displayed = False
    sleep(10)

driver.quit()
