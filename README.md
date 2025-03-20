# Misinformation Video Data Web Scraping

This project aims to create a dataset containing source and veracity information regarding famous online videos as scraped from snopes.com.

## Repository structure information:

### tester.ipynb

This notebook file calls the python scripts from the scraper library **scraper_lib** and tests the correct functioning of the code finally returning the json_results.

### scraper_lib:

This folder contains the python scripts responsible for scraping html data, link extraction and much more.

* article_explorer.py
  
This python file takes url of a single snopes article and extracts all the embedded (possibly) video links in the article using target = _blank. Most of the articles follow the structure of having the first link as the original video source. The script extracts html data from that link and scrapes the title as the representative_text by calling **rep_text** from **scraper_lib**

* link_extractor.py

This script has two methods, **article_soup** extracts all the links from the search results of snopes. **extract_domain** extracts the original domain name where the video was first shared.

* rep_text.py
  
Goes through secondary links and extracts the title information and returns as representative text

* snope_scraper.py
  
The script takes 4 arguments, the combination of these parameters tells the script whether the extraction is being done of the search results from the snopes search results or scrape page source from a list of article links.

### video_downloader.py

This is a prototyping notebook, currently working a script creation aimed at extraction of video from any website. 
**Current approach being followed:**
Searching for video tags does not work for all websites, but for video streams most websites request for **m3u8** files. Extraction of the m3u8 request link from network responses (selenium does not support this, javascript used to extract network responses). 

m3u8 response contains a sequence of short vidoes which can be downloaded and concatenated to create the entire video. 
