from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

item_to_lookup = input("What item would you like to search for? ")

s = Service("/Users/0xrom/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

driver.get("https://oldschool.runescape.com/") 


driver.implicitly_wait(5)
acceptcookie = driver.find_element(By.CLASS_NAME, "CybotCookiebotDialogBodyButton").click()
grandexchange = driver.find_element(By.ID, "osnav-exchange").click()
driver.implicitly_wait(5)
acceptcookie = driver.find_element(By.CLASS_NAME, "CybotCookiebotDialogBodyButton").click()
itemsearch = driver.find_element(By.ID, "item-search")
itemsearch.send_keys(item_to_lookup)
search_item = driver.find_element(By.CLASS_NAME, "search-submit").click()
# result_item = driver.find_elements(By.LINK_TEXT, item_to_lookup).click()
result_items = driver.find_element(By.LINK_TEXT, item_to_lookup.capitalize()).click()
final_price =  driver.find_element(By.XPATH, "//*[@id='grandexchange']/div/div/main/div[2]/div[2]/h3/span").text
# item_price = final_price
print(final_price)
driver.close()
