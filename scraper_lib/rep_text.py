def representative_text(url):
    from selenium import webdriver
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as EC
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.common.action_chains import ActionChains
    from selenium.webdriver.remote.webelement import WebElement
    from selenium.webdriver.support.wait import WebDriverWait
    from selenium.common.exceptions import WebDriverException, TimeoutException
    # from selenium_move_cursor.MouseActions import move_to_element_chrome
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.options import Options
    from bs4 import BeautifulSoup
    from selenium.webdriver.chrome.service import Service
    import time

    opts = webdriver.ChromeOptions()
    opts.add_experimental_option('detach', True)
    opts.add_argument("-—headless")
    driver = webdriver.Chrome(options=opts)

    driver.implicitly_wait(200) # not sequential, global, will wait before returning error, gives time for the js parts to load
    driver.maximize_window()
    while driver.execute_script("return document.readyState;") != "complete":
        time.sleep(1)

    try:
        driver.get(url)          #open the URL
        # JS_get_network_requests = "var performance = window.performance || window.msPerformance || window.webkitPerformance || {}; var network = performance.getEntries() || {}; return network;"
        # network_requests = driver.execute_script(JS_get_network_requests)

        # with open(f'network_requests.txt','w') as file:
        #     file.write(str(network_requests))
        
        time.sleep(2)

        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # with open(f"new_sournce.html", "w", encoding="utf-8") as file: 
        #     file.write(driver.page_source) 

        return [soup.find('head').find('title').text] # network_requests
    except WebDriverException as e: 
        print(f"WebDriverException occurred: {e}")
    except TimeoutException as e:
        print("Page load timed out")

    return "None"
    
        
    