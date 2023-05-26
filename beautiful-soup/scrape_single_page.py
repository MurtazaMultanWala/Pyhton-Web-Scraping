import requests
from bs4 import BeautifulSoup


def save_script_to_file(title, full_script):
    try:
        with open(f"beautiful-soup/scraped_scripts/{title}.txt", "w", encoding="utf-8") as file:
            file.write(full_script)
        print(f"{title}.txt created successfully")
    except Exception:
        print(f"Unable to scrape {title}")


def scrape_and_save_movie_script(movie_page_link):
    page_data = requests.get(movie_page_link)
    page_content = page_data.text
    soup_page_parser = BeautifulSoup(page_content, "lxml")
    try:
        article_box = soup_page_parser.find("article", class_="main-article")
        title = article_box.find("h1").get_text()
        full_script = article_box.find("div", class_="full-script").get_text(strip=True, separator=" ")
        save_script_to_file(title, full_script)
    except Exception as e:
        print(f"Something went wrong while scraping {movie_page_link} err: {e}")


if __name__ == "__main__":
    link = "https://subslikescript.com/movie/Hera_Pheri-73104"
    scrape_and_save_movie_script(link)
