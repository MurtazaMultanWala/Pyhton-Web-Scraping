from bs4 import BeautifulSoup
import requests

from scrape_single_page import scrape_and_save_movie_script

def safe_movie_scripts(movie_links):
    for link in movie_links:
        movie_link = base_link + f'/{link.get("href")}'
        scrape_and_save_movie_script(movie_link)

def scrape_and_safe_movie_scripts_from_movie_lists():
    movies_page_link = base_link + "/movies"
    page_data = requests.get(movies_page_link)  
    page_content = page_data.text
    
    soup_page_parser = BeautifulSoup(page_content, 'lxml')
    
    article_box = soup_page_parser.find("article", class_="main-article")
    movie_list = article_box.find("ul", class_="scripts-list")
    movie_links = movie_list.find_all("a", href=True)
    safe_movie_scripts(movie_links)


if __name__ == "__main__":
    base_link = "https://subslikescript.com" 
    scrape_and_safe_movie_scripts_from_movie_lists()