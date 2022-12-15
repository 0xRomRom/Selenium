from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)


s = Service("/Users/0xrom/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://random-generators.com") 

clickr = driver.find_element(By.CLASS_NAME, "NumberGenerator_generate__OBrbg")
clickr.send_keys(Keys.RETURN)
clickr.send_keys(Keys.RETURN)
clickr.send_keys(Keys.RETURN)
clickr.send_keys(Keys.RETURN)
clickr.send_keys(Keys.RETURN)

# driver.quit()