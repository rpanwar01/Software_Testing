from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def test_that_toasters_appear_in_search_at_correct_price_and_rating(browser):
	# Customer goes to Google
	browser.get("http://www.google.com")
	assert "Google" in browser.title	
	
	# customer enters "toaster" in the search box
	search_box = browser.find_element_by_name("q")
	search_box.send_keys("toaster")
	search_box.send_keys(Keys.RETURN)
	
	# Amazon appears in the first page of results
	browser.implicitly_wait(4)
	results = browser.find_element_by_id("ires")
	targets = results.find_elements_by_tag_name("a")
	link = None
	for target in targets:
		if target.get_attribute("href").startswith("http://www.amazon.com"):
			link = target.get_attribute("href")
	assert link != None
		
	# Customer clicks the Amazon link
	browser.get(link)
	browser.implicitly_wait(4)
	assert "Amazon" in browser.title	
	
	# Page of toasters appears
	assert "Toasters" in browser.page_source
	
	# Our toaster is on the page
	assert "Oster" in browser.page_source
	items = browser.find_elements_by_class_name("celwidget")
	oster_item = None
	position = 0
	n = 0
	for item in items:
		n = n + 1
		if "Oster" in item.text:
			oster_item = item 
			position = n
			break
	assert oster_item != None
	
	# toaster is in the top 4
	assert position <= 4

	# Our toaster is less than $40.00
	text = oster_item.text
	lowest_price = 10000000000000.00
	for line in text.split("\n"):
		if line.startswith("$"):
			line = line.replace("$","")
			if " " in line:
				line = line.split(" ")[0]
			value = float(line)
			if value < lowest_price:
				lowest_price = value
	assert lowest_price < 40.00		

	# Customer searches for 4-slice on that page
	search_box = browser.find_element_by_id("twotabsearchtextbox")
	search_box.send_keys("4-slice")
	search_box.send_keys(Keys.RETURN)

	# Our toaster is one of the top 2 results
	assert "Oster" in browser.page_source
	items = browser.find_elements_by_class_name("celwidget")
	oster_item = None
	position = 0
	n = 0
	for item in items:
		n = n + 1
		if "Oster" in item.text:
			oster_item = item 
			position = n
			break
	assert oster_item != None
	
	# toaster is in the top 2
	assert position <= 2

	# Our 4-slice toaster gets review of 4 stars or higher
	star_items = oster_item.find_elements_by_class_name("a-icon-star")
	for star_item in star_items:
		print(star_item.text)

	print("pass")


options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument('--disable-application-cache')
browser = webdriver.Chrome(chrome_options=options)

test_that_toasters_appear_in_search_at_correct_price_and_rating(browser)

time.sleep(3)

browser.close()	

#driver = webdriver.Firefox()
#driver.get("http://www.python.org")
#assert "Python" in driver.title
#elem = driver.find_element_by_name("q")
#elem.send_keys("pycon")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
#driver.close()