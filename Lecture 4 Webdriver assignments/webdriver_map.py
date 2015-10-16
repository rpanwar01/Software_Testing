from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Test to check the distance between two places by drive and walk
def test_to_check_the_distance_between_two_places(browser):
	# Go to Google
	browser.get("http://www.google.com")
	assert "Google" in browser.title	
	
	# Enter "maps" in the search box
	search_box = browser.find_element_by_name("q")
	search_box.send_keys("maps")
	search_box.send_keys(Keys.RETURN)
	
	# Google Maps appears in the first page of results
	browser.implicitly_wait(4)
	results = browser.find_element_by_link_text('Google Maps')
	results.click()

	# Click on the Google Maps and enter the search criteria
	search_box = browser.find_element_by_name("q")
	search_box.send_keys("Cleveland, OH to Kent, OH")
	search_box.send_keys(Keys.RETURN)

	# Check for the drive (by car) option and click
	browser.implicitly_wait(4)
	browser.find_element_by_class_name("directions-drive-icon").click()

	# Check for the first link with the minimum duration and click
	time.sleep(2)	
	browser.implicitly_wait(5)
	browser.find_element_by_class_name("widget-pane-section-directions-trip-numbers").click()

	# Read the text with given distance and print
	browser.implicitly_wait(4)
	values = browser.find_element_by_class_name("widget-pane-section-trip-summary-title")
	print("Distance between Cleveland ohio to Kent ohio by car is " + values.text)
	
	# Click on back button on map
	browser.find_element_by_class_name("maps-sprite-common-arrow-back-white").click()
	
	# Check for the Walking option and click
	time.sleep(2)	
	browser.find_element_by_class_name("directions-walk-icon").click()
	
	# Check for the first link with the minimum duration and click
	time.sleep(2)	
	browser.implicitly_wait(5)
	browser.find_element_by_css_selector(".widget-pane-section-directions-trip.selected").click()

	# Read the text with given distance and print
	browser.implicitly_wait(4)
	value = browser.find_element_by_class_name("widget-pane-section-trip-summary-title")
	print("Distance between Cleveland ohio to Kent ohio by Walk is " + value.text)
	
	# Check weather side panel working fine
	browser.find_element_by_class_name("widget-pane-toggle-button-container").click()

	
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument('--disable-application-cache')
browser = webdriver.Chrome(chrome_options=options)

test_to_check_the_distance_between_two_places(browser)

time.sleep(10)

browser.close()	
