#!/usr/bin/env python
# coding: utf-8

# Dependencies
from bs4 import BeautifulSoup
import requests
from splinter import Browser
from pprint import pprint 
import pandas as pd
import time


def scrape():
	executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
	browser = Browser('chrome', **executable_path, headless=False)


	# https://mars.nasa.gov/news/ to be scraped
	nasa_news_url = 'https://mars.nasa.gov/news/'
	browser.visit(nasa_news_url)

	# Create BeautifulSoup object; parse with 'html.parser'
	time.sleep(5)
	html = browser.html
	soup = BeautifulSoup(html, 'html.parser')


	# results are returned as an iterable list
	results = soup.find_all('li', class_="slide")


	# Loop through returned results
	for result in results:
		try:
			# Identify and return title of listing
			news_title = result.find('div', class_ ='list_text').find('a').text
			# Identify and return title of listing
			news_p = result.find('div', class_="article_teaser_body").text
			
			if (news_title and news_p):
				print('-------------')
				print(news_title)
				print(news_p)
				
				break
			
		except AttributeError as e:
			print(e)


	# https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars to be scraped
	jpl_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
	browser.visit(jpl_url)
	ime.sleep(5)

	browser.click_link_by_partial_text("FULL IMAGE")
	time.sleep(5)

	browser.click_link_by_partial_text("more info")
	time.sleep(5)

	html = browser.html
	jpl_image_soup = BeautifulSoup(html, 'html.parser')

	featured_image_url = jpl_image_soup.find_all('div', class_="download_tiff")
	jpl_jpg_image = featured_image_url[1].a.get('href')
	print('https:' + jpl_jpg_image)

	# https://twitter.com/marswxreport?lang=en to be scraped
	mars_twitter_url = 'https://twitter.com/marswxreport?lang=en'
	browser.visit(mars_twitter_url)
	time.sleep(5)

	weather_html = browser.html
	mars_weather_soup = BeautifulSoup(weather_html, 'html.parser')

	mars_weather_posts = mars_weather_soup.find_all("span", class_="css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0")
	for post in mars_weather_posts:
    		if "InSight sol" in post.text:
        		mars_weather = post.text
        		break
	print(mars_weather)


	mars_facts_url = 'https://space-facts.com/mars/'
	browser.visit(mars_facts_url)
	time.sleep(5)


	tables = pd.read_html(mars_facts_url)
	tables

	type(tables)

	df = tables[0]
	df

	html_table = df.to_html()
	html_table


	html_table.replace('\n', '')

	hemisphere_dict = {}


	hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
	browser.visit(hem_url)
	time.sleep(5)
	html = browser.html


	link = browser.find_link_by_partial_text('Hemisphere Enhanced')[0]
	link.click()
	title = browser.find_by_css('.title').first.text
	url = browser.find_by_text('Sample').first["href"]
	print(title)
	print(url)
	browser.back()
	hemisphere_dict[url] = title

	link = browser.find_link_by_partial_text('Hemisphere Enhanced')[1]
	link.click()
	title = browser.find_by_css('.title').first.text
	url = browser.find_by_text('Sample').first["href"]	
	print(title)
	print(url)
	browser.back()
	hemisphere_dict[url] = title

	link = browser.find_link_by_partial_text('Hemisphere Enhanced')[2]
	link.click()
	title = browser.find_by_css('.title').first.text
	url = browser.find_by_text('Sample').first["href"]
	print(title)
	print(url)
	browser.back()
	hemisphere_dict[url] = title

	link = browser.find_link_by_partial_text('Hemisphere Enhanced')[3]
	link.click()
	title = browser.find_by_css('.title').first.text
	url = browser.find_by_text('Sample').first["href"]
	print(title)
	print(url)
	browser.back()
	hemisphere_dict[url] = title

	hemisphere_dict

	data = {"News_Header":news_title,"News_Article":news_p,"JPL_Image":jpl_jpg_image,"Weather":mars_weather,"Facts":df,"Hemispheres":hemisphere_dict}
	
	return data
# scrape()


