from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # browser = init_browser()
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    mars = {}

    url = "https://redplanetscience.com/"
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

    mars["headlines"] = soup.find('div',class_="content_title").get_text()
    mars["article"] = soup.find('div',class_="article_teaser_body").get_text()
    mars["date"] = soup.find('div', class_="list_date").get_text()

    # Quit the browser
    browser.quit()

    return mars
