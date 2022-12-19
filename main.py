from selenium import webdriver
from time import sleep
import csv

from selenium.webdriver.common.keys import Keys

from driver import Driver
from pages.google import GooglePage


next_btn_displayed = True
init_driver = Driver()
all_results = []


def check_captcha():
    try:
        captcha = gpage.captcha_element()
        if captcha.is_displayed():
            sleep(120)
    except:
        print("captcha not displayed")


def search_postition(title, company):
    search_input = gpage.search_input_element()
    search_input.send_keys(
        f"site:in.linkedin.com/in intitle:{title} {company}", Keys.ENTER
    )
    check_captcha()


def click_on_next():
    try:
        next_button = gpage.next_button()
        next_button.click()
    except:
        next_btn_displayed = False


def write_csv():
    with open(f"{company_name} - {job_title}.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)
        writer.writerow(["title", "link"])
        for result in all_results:
            writer.writerow(result)


if __name__ == "__main__":
    company_name = input("Enter a company name: ")
    job_title = input("Enter job title: ")
    driver = init_driver.start_chrome_driver()
    driver.delete_all_cookies()
    driver.get("https://www.google.com")
    gpage = GooglePage(driver)
    search_postition(job_title, company_name)
    count = 0
    while count != 10:
        titles = gpage.result_title_list()
        links = gpage.result_link_list()
        for (title, link) in zip(titles, links):
            all_results.append([title.text, link.get_attribute("href")])
        click_on_next()
        if next_btn_displayed is False:
            break
        count += 1
        check_captcha()
        sleep(10)
    write_csv()
    init_driver.close_driver()
