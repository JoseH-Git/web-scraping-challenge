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
    
    mars_news = []
    
    for x in range(100):
        dictionary = {"title":headlines[x].text,"article":article[x].text}
        mars_news.append(dictionary)
    browser.quit()

    # Quit the browser
    browser.quit()

    url = "https://spaceimages-mars.com/"
    browser.visit(url)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    images_list = []
    general_scrape_images = soup.body.find('div',class_='thmbgroup')
    images = general_scrape_images.find_all('a')
    for image in images:
        images_list.append(url+image['href'])
    images_list
    
    # Quit the browser
    browser.quit()

    url = 'https://marshemispheres.com/'
    browser.visit(url)
    html = browser.html

    hemisphere_scrape_links = soup.body.find('div',class_='collapsible results')
    hemisphere_links = hemisphere_scrape_links.find_all('a',class_="itemLink product-item")
    hemisphere_images = []
    for link in hemisphere_links:
        image_dict = {}
        if link.h3 is None:
            link_path = link["href"]
            browser.visit(url+link_path)
            html = browser.html
            soup = BeautifulSoup(html, 'html.parser')
            title = soup.body.find('h2',class_="title").text
            hem_image = soup.body.find('img',class_='wide-image')['src']
            image_dict["title"] = title
            image_dict["img_url"] = url+hem_image
            hemisphere_images.append(image_dict)

    hemisphere_images

    print(hemisphere_images)

