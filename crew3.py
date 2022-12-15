from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# import Action chains 
from selenium.webdriver.common.action_chains import ActionChains

# Make sure window stays open
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_extension('/Users/0xrom/Desktop/MetaMask.crx')



# Specify path and configure chrome
s = Service("/Users/0xrom/Downloads/chromedriver.exe")
driver = webdriver.Chrome(service=s, options=chrome_options)

# Get URL
driver.get("https://crew3.xyz/") 

# Create chain to navigate to the first modal
driver.switch_to.window('main')
driver.implicitly_wait(5)



accept_cookies = driver.find_element(By.XPATH, "//*[@id='app']/div[2]/button").click()
actions = ActionChains(driver) 
zkSync = driver.find_element(By.XPATH, "//*[@id='communities']/div[2]/a[1]/div[1]")
actions.scroll_to_element(zkSync)
actions.click(zkSync)
actions.perform()
driver.implicitly_wait(3)

# On zkSync page

twitter_task = driver.find_element(By.XPATH, '//*[@id="8e062424-fa21-4d5a-b295-a7c6de0410fe"]').click()
driver.implicitly_wait(6)
connect_wallet = driver.find_element(By.XPATH, "//*[contains(text(), 'Connect to claim')]").click()
driver.implicitly_wait(6)
select_metamask = driver.find_element(By. CLASS_NAME, 'kPJKao').click()
driver.implicitly_wait(7)


# On metamask page

get_started = driver.find_element(By. XPATH, '//*[@id="app-content"]/div/div[2]/div/div/div/button').click()







