from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import requests


def scrape():
    #Mars News
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    listings = {}

    url = "https://redplanetscience.com"
    browser.visit(url)
    time.sleep(1)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    listings["title"] = soup.find("div", class_="content_title").get_text()
    listings["article"] = soup.find("h4", class_="wysiwyg_content").get_text()
    listings["date"] = soup.find("div", class_="list_date").get_text()

    # Quit the browser
    browser.quit()

    return listings
