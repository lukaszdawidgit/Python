import re
from selenium import common
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def extract_hashtags(text):
    pattern = "#(\w+)"
    return re.findall(pattern, text)

hashtags = []

driver = webdriver.Chrome('./chromedriver.exe')
driver.get('https://twitter.com/hashtag/python')

posts_loaded = expected_conditions.presence_of_element_located((By.TAG_NAME, 'article'))
WebDriverWait(driver, 30).until(posts_loaded)

for post in driver.find_elements(by=By.TAG_NAME, value='article'):
    try:
        hashtags += extract_hashtags(post.find_element(by=By.CSS_SELECTOR, value='[lang="en"]').text)
    except common.exceptions.NoSuchElementException:
        continue

counter = {}
for hashtags in hashtags:
    if hashtags not in counter:
        counter[hashtags] = 0

print(hashtags)
print(counter)
driver.stop_client()
