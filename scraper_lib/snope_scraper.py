def scraper(num_pages, scrape_search = True, scrape_article = False, article_url_list = None):
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

    driver.implicitly_wait(200) # not sequential, global, will wait before returning error, gives time for the js parts to load
    driver.maximize_window() #maximize the window

    if scrape_search:
        html_results = []

        base_url = 'https://www.snopes.com/search/?cx=partner-pub-6610802604051523%3Aamzitfn8e7v&cof=FORID%3A10&ie=ISO-8859-1&siteurl=&ref=&ss=&q=video#gsc.tab=0&gsc.q=video&gsc.page='
        if num_pages == 1:
            driver.get(f"{base_url}1")
            time.sleep(2)
            page_source = driver.page_source
            driver.quit()
            # driver.close()
            return [page_source] 

        # number of result pages to be scraped
        for i in range (1,num_pages,1):
            driver.get(f"{base_url}{i}")          #open the URL
            page_source = driver.page_source
            html_results.append(page_source)
            time.sleep(2)

            # with open(f"page_source{i}.html", "w", encoding="utf-8") as file: 
            #     file.write(driver.page_source)  ## IMPORTANT: we are leveraging this to find articles using BeautifulSoup

        time.sleep(2)
        driver.quit()
        # driver.close()
        return html_results
    
    elif scrape_article:

        article_results = []

        for article_url in article_url_list:
            if article_url == None:
                continue
            driver.get(article_url)
            page_source = driver.page_source
            article_results.append(page_source)
            time.sleep(2)
        
        driver.quit()

        return article_results