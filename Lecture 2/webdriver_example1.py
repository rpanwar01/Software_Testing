from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    
    driver = webdriver.Firefox()
    #driver.get("http://www.python.org")
    driver.get("http://www.google.com")
    assert "Google" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("kent state")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()