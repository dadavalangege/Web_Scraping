from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.firefox.options import Options


firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.privatebrowsing.autostart", True)

opts = Options()
opts.headless = True
assert opts.headless 

browser = webdriver.Firefox(options=opts, firefox_profile=firefox_profile)
driver.get("https://www.bolsamadrid.es")
assert "Bolsa de Madrid" in driver.title
elem = driver.find_element_by_class_name("Acciones")
elem.click()
#elem.send_keys("")
#elem.send_keys(Keys.RETURN)
#assert "No results found." not in driver.page_source
driver.close()