from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


s = Service("/Users/0xrom/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("http://www.python.org") 