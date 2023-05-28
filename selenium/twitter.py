import time

import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from bootstrap import get_chrome_driver
from constants import Constant
from models.tweet import Tweet

profile_link = "https://twitter.com/MindPsychology_/status/1660578827368644613"
driver = get_chrome_driver()
driver.maximize_window()
driver.get(profile_link)
scraped_tweet_ids = set()
all_tweets = []


def get_tweet_details(tweet):
    username = tweet.find_element(By.XPATH, ".//span[contains(text() , '@')]").text
    content = tweet.find_element(By.XPATH, ".//div[@lang]").text
    content = " ".join(content.split())
    tweet = Tweet(username=username, tweet_content=content)
    return tweet, tweet.username + tweet.tweet_content


def scrape_tweets(tweets_list):
    for tweet in tweets_list:
        try:
            tweet_obj, unique_id = get_tweet_details(tweet)
            if unique_id not in scraped_tweet_ids:
                all_tweets.append(tweet_obj)
                scraped_tweet_ids.add(unique_id)
        except:
            continue


if __name__ == "__main__":
    current_page_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        tweets = WebDriverWait(driver, Constant.DELAY_IN_SECONDS.value).until(
            EC.presence_of_all_elements_located((By.XPATH, "//article[@role='article']"))
        )
        scrape_tweets(tweets)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        new_page_height = driver.execute_script("return document.body.scrollHeight")
        if current_page_height == new_page_height:
            break
        current_page_height = new_page_height

tweets_df = pd.DataFrame([tweet.to_dict() for tweet in all_tweets])
tweets_df.to_csv("selenium/scraped_data/tweets.csv", index=False)
driver.quit()
