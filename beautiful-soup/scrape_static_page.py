from bs4 import BeautifulSoup
import requests

link = "https://subslikescript.com/movie/Hera_Pheri-73104" 
page_data = requests.get(link)
page_content = page_data.text

soup_page_parser = BeautifulSoup(page_content, "lxml")

article_box = soup_page_parser.find("article", class_="main-article")
title = article_box.find("h1").get_text()

full_script = article_box.find("div", class_="full-script").get_text(strip=True, separator=" ")

with open(f"beautiful-soup/{title}.txt", "w") as file:
    file.write(full_script)
print(f"{title}.txt created successfully")