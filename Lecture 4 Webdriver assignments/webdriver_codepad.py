from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Test to check the python sysntax using codepad.org
def test_to_check_the_python_syntax_using_codepad(browser):
	# Go to Codepad.org
	browser.get("http://codepad.org")
	assert "codepad" in browser.title	
	
	# Select the Python language option
	python_link = browser.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
	python_link.click()
	
	# Enter some code for testing!
	text_area = browser.find_element_by_id('textarea')
	text_area.send_keys("print 'Test code for Webdriver Program!'")
	# text_area.send_keys("print Test code for Webdriver Program!") - Incorrect Syntax
	
	# Submit the form!
	submit_button = browser.find_element_by_name('submit')
	submit_button.click()
	
	# Check weather syntax (for code you entered) is correct or not
	try:
		assert "Test code for Webdriver Program!" in browser.get_page_source()
		print ("Syntax is correct..!!")
	except:
		print ("Syntax is not correct..!!")
	return True
	
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument('--disable-application-cache')
browser = webdriver.Chrome(chrome_options=options)

test_to_check_the_python_syntax_using_codepad(browser)

time.sleep(10)

browser.close()	
