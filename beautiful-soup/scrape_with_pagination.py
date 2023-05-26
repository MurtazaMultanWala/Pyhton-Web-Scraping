from scrape_multiple_pages import get_movies_page_content, scrape_movie_scripts


def get_total_pages(movies_page_url):
    movies_page_content = get_movies_page_content(movies_page_url)
    pagination_content = movies_page_content.find("nav", class_="pagination_pages")
    pages_navbar = pagination_content.find_all("li", class_="page-item")
    last_page = pages_navbar[-2].get_text()
    return int(last_page)


def scrape_and_save_with_pagination(movies_page_base_url, pages=1):
    for page_no in range(1, pages + 1):
        page_link = f"{movies_page_base_url}?page={page_no}"
        scrape_movie_scripts(page_link)


if __name__ == "__main__":
    movies_page_base_link = "https://subslikescript.com/movies"
    try:
        total_pages = get_total_pages(movies_page_base_link)
        scrape_and_save_with_pagination(movies_page_base_link, total_pages)
    except Exception as e:
        print(f"Something went wrong err: {e}")
