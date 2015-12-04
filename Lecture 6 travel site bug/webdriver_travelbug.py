from selenium import webdriver
import requests
from selenium.webdriver.common.keys import Keys
import time

# Test to reproduce the bug/error in flyfrontier site
def test_to_reproduce_bug_in_a_travel_site(browser):
	# Go to Frontier Airlines
	browser.get("https://booking.flyfrontier.com/Flight/#flightStatus-tab")
	assert "Frontier Airlines" in browser.title	

	# Click on Check flight status by flight number
	browser.implicitly_wait(4)
	browser.find_element_by_id("byFlightNumberToggle").click()
	
	# Enter the flight number
	search_box = browser.find_element_by_id("flightScheduleSearch_FlightNumber")
	#search_box.send_keys("287") - valid Flight number
	search_box.send_keys("Ind1234")
	search_box.send_keys(Keys.RETURN)
	
	# Verify for the error
	#r = requests.get("https://booking.flyfrontier.com/Flight/Status")
	#print (r.status_code)
	try:
		value = browser.find_element_by_class_name("alert-heading").text
		if value == 'ERRORS':
			print ("There is an Error... Error verification is done..!!")
	except:
		return
	return True
	
	
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument('--disable-application-cache')
browser = webdriver.Chrome(chrome_options=options)

test_to_reproduce_bug_in_a_travel_site(browser)

time.sleep(10)

browser.close()	
