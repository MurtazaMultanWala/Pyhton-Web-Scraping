import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from constants import Constant
from bootstrap import get_chrome_driver
from model.product import Product


def get_scraped_page_products(products):
    products_list = []
    for product in products:
        title = product.find_element(By.TAG_NAME, "h3").text

        author = product.find_element(By.XPATH, ".//li[contains(@class, 'authorLabel')]").text
        author = str(author.split(":")[1]).strip()

        duration = product.find_element(By.XPATH, ".//li[contains(@class, 'runtimeLabel')]").text
        duration = str(duration.split(":")[1]).strip()

        release_date = product.find_element(By.XPATH, ".//li[contains(@class, 'releaseDateLabel')]").text
        release_date = str(release_date.split(":")[1]).strip()

        product_obj = Product(title=title, author=author, duration=duration, release_date=release_date)
        products_list.append(product_obj)
    return products_list


if __name__ == "__main__":
    audible_website = "https://www.audible.com/search"
    driver = get_chrome_driver()
    driver.maximize_window()
    driver.get(audible_website)

    pagination = driver.find_elements(By.XPATH, "//ul[contains(@class, 'pagingElements')]/li")
    total_product_pages = int(pagination[-2].text)

    current_page = 1
    product_details = []
    while current_page <= total_product_pages:
        product_list = driver.find_elements(By.XPATH, "//li[contains(@class, 'productListItem')]")
        page_products = get_scraped_page_products(product_list)
        product_details.extend(page_products)
        print(f"Page# {current_page} scraped successfully")

        current_page += 1
        next_button = driver.find_element(By.XPATH, "//span[contains(@class, 'nextButton')]/a")
        next_button.click()
        WebDriverWait(driver, Constant.DELAY_IN_SECONDS.value).until(EC.presence_of_element_located((By.CLASS_NAME, "productListItem")))

    print(f"Saving {len(product_details)} products to csv file...")
    product_df = pd.DataFrame([product.to_dict() for product in product_details])
    product_df.to_csv("selenium/scraped_data/product_list.csv", index=False)
    print("Record saved to csv file")
    driver.quit()
