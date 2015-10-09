from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.amazon.com")
assert "Amazon" in driver.title
elem = driver.find_element_by_name("field-keywords")
elem.send_keys("Coffee Mugs")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()
