from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
# from selenium_move_cursor.MouseActions import move_to_element_chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import numpy as np
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
import time

# open the browser
opts = webdriver.ChromeOptions()
opts.add_experimental_option('detach', True)
opts.add_argument("-—headless")
driver = webdriver.Chrome(options=opts)

# # search the url
base_url = 'https://www.snopes.com/search/?cx=partner-pub-6610802604051523%3Aamzitfn8e7v&cof=FORID%3A10&ie=ISO-8859-1&siteurl=&ref=&ss=&q=video#gsc.tab=0&gsc.q=video&gsc.page='
driver.implicitly_wait(200) # not sequential, global, will wait before returning error, gives time for the js parts to load
driver.maximize_window() #maximize the window

for i in range (1,5,1):
    time.sleep(8)
    driver.get(f"{base_url}{i}")          #open the URL
    with open(f"page_source{i}.html", "w", encoding="utf-8") as file: 
        file.write(driver.page_source)  ## IMPORTANT: we are leveraging this to find articles using BeautifulSoup

# # scroll down to open the whole page
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")



# print(driver.page_source)
# driver.save_screenshot('attempt1.png')

# search_result = driver.find_element(By.CSS_SELECTOR, '.gs-title')
# print(search_result.text)

# with open("search_results.txt", "w", encoding="utf-8") as result_file:
#     result_file.write(search_result.text)

# chrm_options = Options()
# chrm_options.add_experimental_option('detach', True)
# driver = webdriver.Chrome(options=chrm_options)
# driver.get('https://www.google.com')