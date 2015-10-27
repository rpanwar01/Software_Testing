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
			print(res_count)
	
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
			print(res_count1)

# Executing original catalog test in Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument('--disable-application-cache')
browser = webdriver.Chrome(chrome_options=options)

test_to_check_the_result_count_for_original_catlog(browser)
time.sleep(2)
browser.close()		
			
# Executing new catalog test in Chrome
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument('--disable-application-cache')
browser = webdriver.Chrome(chrome_options=options)

test_to_check_the_result_count_for_new_catlog(browser)
time.sleep(2)
browser.close()	

if res_count1 >= res_count:
	print("Test Pass - Result count in new catalog is equal to or greater than original catalog")
else:
	print("Test Fail- Result count in new catalog is less than original catalog"")