from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

res_count = 0
res_count1 = 0

# Prototype for nypl catalog testing

def test_to_check_the_result_count_for_original_catlog(browser):
	# # Go to original NYPL catalog
	browser.get("http://catalog.nypl.org")
	assert "New York Public Library Catalog" in browser.title	
	
	# customer enters "Indian Art" in the search box
	search_box = browser.find_element_by_name("searcharg")
	search_box.send_keys("Indian Art")
	search_box.send_keys(Keys.RETURN)
	
	# fetch the search result count
	time.sleep(2)	
	browser.implicitly_wait(5)
	values = browser.find_element_by_class_name("browseSearchtoolMessage")
	Texts = values.text.split(" ", 1)
	n = 0
	for Text in Texts:
		n = n + 1
		if n ==1:
			res_count = Text
#			print("Result count of original Catalog : " , res_count)
			
def test_to_check_the_option_to_refine_by_availibility_original(browser):
	browser.implicitly_wait(2)	
	try:
		assert "availability" in browser.page_source
	except:
		print("Original Catalog doesn't have option to refine by Availibility")
	return True
	
def test_to_check_the_option_to_refine_by_format_original(browser):	
	try:
		assert "formate" in browser.page_source
	except:
		print("Original Catalog doesn't have option to refine by Format")
	return True

def test_to_check_the_option_to_refine_by_language_original(browser):	
	try:
		assert "Lang" in browser.page_source
	except:
		print("Original Catalog doesn't have option to refine by Language")
	return True

def test_to_check_the_option_to_sort_by_date_original(browser):	
	link = browser.find_element_by_link_text('date')
	link.click()
	print("Sort by date option works fine in Original Catalog")
	
def test_to_check_the_option_to_sort_by_title_original(browser):	
	time.sleep(2)	
	browser.implicitly_wait(5)
	link = browser.find_element_by_link_text('title')
	link.click()
	print("Sort by title option works fine in Original Catalog")	
			
def test_to_check_the_option_to_search_by_ISBN_original(browser):
	
	results = browser.find_element_by_link_text('By ISBN')
	results.click()
	# customer enters "ISBN Number" in the search box
	search_box = browser.find_element_by_name("SEARCH")
	search_box.send_keys("0545139708")
	search_box.send_keys(Keys.RETURN)
	
	assert "Harry Potter and the deathly hallows / by J.K. Rowling ; illustrations by Mary GrandPré." in browser.page_source
	print("Search a book by an ISBN number works fine in Original Catalog")
	
def test_to_check_the_result_for_SQL_injection_original(browser):
	
	Keyword = '"Select * from user"'
	
	# customer enters "SQL injection" in the search box
	search_box = browser.find_element_by_name("searcharg")
	search_box.send_keys(Keyword)
	search_box.send_keys(Keys.RETURN)
	
	browser.implicitly_wait(3)
	assert "NO ENTRIES FOUND" in browser.page_source
	print("Original Catalog doens't entertain any SQL injections")
	
def test_to_check_the_option_save_the_record_original(browser):
	
	try:
		link = browser.find_element_by_link_text('Save This Record')
		link.click()
	except:
		print("Original Catalog doesn't have option to save the record")
	return True
	
def test_to_check_the_option_Email_the_record_original(browser):
	try:
		link = browser.find_element_by_link_text('Email This Record')
		link.click()
	except:
		print("Original Catalog doesn't have option to email the record")
	return True	
	
def test_to_check_the_result_count_for_new_catlog(browser):
	# Go to new NYPL catalog
	browser.get("http://browse.nypl.org")
	assert "NYPL Catalog" in browser.title	
	
	# customer enters "Indian Art" in the search box
	search_box = browser.find_element_by_name("searchString")
	search_box.send_keys("Indian Art")
	search_box.send_keys(Keys.RETURN)
	
	# fetch the search result count
	time.sleep(3)	
	browser.implicitly_wait(5)
	values = browser.find_element_by_class_name("noResultsHideMessage")
	Texts = values.text.split(" ")
	n = 0
	for Text in Texts:
		n = n + 1
		if n ==6:
			res_count1 = Text
#			print("Result count of new Catalog : " ,res_count1)

def test_to_check_the_option_to_refine_by_availibility_new(browser):
	time.sleep(2)
	browser.implicitly_wait(4)	
	assert "Availability" in browser.page_source
	print("New Catalog has the option to refine by Availibility")

def test_to_check_the_option_to_refine_by_format_new(browser):	
	assert "Format" in browser.page_source		
	print("New Catalog has the option to refine by Format")
	
def test_to_check_the_option_to_refine_by_language_new(browser):	
	assert "Language" in browser.page_source
	print("New Catalog has the option to refine by language")		

def test_to_check_the_option_to_sort_by_date_new(browser):	
	link = browser.find_element_by_link_text('Date')
	link.click()
	print("Sort by date option works fine in New Catalog")

def test_to_check_the_option_to_sort_by_title_new(browser):	
	time.sleep(2)	
	browser.implicitly_wait(5)
	link = browser.find_element_by_link_text('Title')
	link.click()
	print("Sort by title option works fine in New Catalog")

def test_to_check_the_option_to_search_by_ISBN_new(browser):
	
	# customer enters "ISBN Number" in the search box
	search_box = browser.find_element_by_name("searchString")
	search_box.send_keys("0545139708")
	search_box.send_keys(Keys.RETURN)
	
	browser.implicitly_wait(3)
	assert "Harry Potter and the deathly hallows" in browser.page_source
	print("Search a book by an ISBN number works fine in New Catalog")
	
def test_to_check_the_result_for_SQL_injection_new(browser):
	
	Keyword = "Indian art""Select * from user"
	
	# customer enters "SQL injection" in the search box
	search_box = browser.find_element_by_name("searchString")
	search_box.send_keys(Keyword)
	search_box.send_keys(Keys.RETURN)
	
	browser.implicitly_wait(3)
	assert "No catalog results found." in browser.page_source
	print("New Catalog doens't entertain any SQL injections")

def test_to_check_the_option_save_the_record_new(browser):
	
	# customer enters "Indian Art" in the search box
	search_box = browser.find_element_by_name("searchString")
	search_box.send_keys("Indian Art")
	search_box.send_keys(Keys.RETURN)
	
	book_cart = browser.find_element_by_id("addToBookcartImageAnyComponent")
	book_cart.click()
	
	time.sleep(3)
	browser.implicitly_wait(5)
	assert "This item is in your book bag" in browser.page_source
	print("New Catalog has the option to save the record")
	
def test_to_check_the_option_Email_the_record_new(browser):
	
	book_cart = browser.find_element_by_id("emailImageAnyComponent")
	book_cart.click()
	
	time.sleep(3)
	browser.implicitly_wait(3)
	search_box = browser.find_element_by_name("emailTextInput")
	search_box.send_keys("rpanwar@kent.edu")
	search_box.send_keys(Keys.RETURN)
	
	time.sleep(2)
	assert "Your email has been sent." in browser.page_source
	results = browser.find_element_by_link_text('OK')
	results.click()
	print("New Catalog has the option to Email the record")
								
# Executing original catalog test in Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument('--disable-application-cache')
browser = webdriver.Chrome(chrome_options=options)

print("Test results for Original Catalog :")
test_to_check_the_result_count_for_original_catlog(browser)
test_to_check_the_option_to_refine_by_availibility_original(browser)
test_to_check_the_option_to_refine_by_format_original(browser)
test_to_check_the_option_to_refine_by_language_original(browser)
test_to_check_the_option_to_sort_by_date_original(browser)
test_to_check_the_option_to_sort_by_title_original(browser)
test_to_check_the_option_save_the_record_original(browser)
test_to_check_the_option_Email_the_record_original(browser)
test_to_check_the_result_for_SQL_injection_original(browser)
test_to_check_the_option_to_search_by_ISBN_original(browser)
time.sleep(2)
browser.close()	

# Executing new catalog test in Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument('--disable-application-cache')
browser = webdriver.Chrome(chrome_options=options)

print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
print("Test results for New Catalog :")
test_to_check_the_result_count_for_new_catlog(browser)
test_to_check_the_option_to_refine_by_availibility_new(browser)
test_to_check_the_option_to_refine_by_format_new(browser)
test_to_check_the_option_to_refine_by_language_new(browser)
test_to_check_the_option_to_sort_by_date_new(browser)
test_to_check_the_option_to_sort_by_title_new(browser)
test_to_check_the_option_to_search_by_ISBN_new(browser)
test_to_check_the_result_for_SQL_injection_new(browser)
test_to_check_the_option_save_the_record_new(browser)
test_to_check_the_option_Email_the_record_new(browser)
time.sleep(2)
browser.close()

if res_count1 >= res_count:
	print("Result count in new catalog is equal to or greater than original catalog for a given keyword.")

