from bs4 import BeautifulSoup
import requests

from scrape_single_page import scrape_and_save_movie_script

base_link = "https://subslikescript.com"

def save_movie_scripts(movie_links):
    for link in movie_links:
        movie_link = base_link + f'/{link.get("href")}'
        scrape_and_save_movie_script(movie_link)
        
def get_movies_page_content(movies_page_link) -> BeautifulSoup:
    page_data = requests.get(movies_page_link)  
    page_content = page_data.text
    
    soup_page_parser = BeautifulSoup(page_content, 'lxml')
    return soup_page_parser

def scrape_movie_scripts(movies_page_link):
    soup_page_parser = get_movies_page_content(movies_page_link)
    article_box = soup_page_parser.find("article", class_="main-article")
    movie_list = article_box.find("ul", class_="scripts-list")
    movie_links = movie_list.find_all("a", href=True)
    save_movie_scripts(movie_links)


if __name__ == "__main__":
    movies_page_link = base_link + "/movies"
    scrape_movie_scripts(movies_page_link)