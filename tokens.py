from selenium import webdriver
import os
import random
import time

print("started....")
driver_path = "./chromedriver.exe"
brave_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"

option = webdriver.ChromeOptions()
option.binary_location = brave_path
option.add_argument("--user-data-dir=C:/Users/vinayaka s sajjan/AppData/Local/BraveSoftware/Brave-Browser/User Data")
#option.add_argument("--incognito")
# option.add_argument("--headless") OPTIONAL

# Create new Instance of Chrome
browser = webdriver.Chrome(executable_path=driver_path, chrome_options=option)
'''
browser.get("https://www.google.com")
browser.execute_script("window.open('');")
browser.switch_to.window(browser.window_handles[1])
browser.get("https://brave.com")

browser.close()

browser.switch_to.window(browser.window_handles[0]) '''

urls = {
0 : "https://www.google.com",
1 : "https://shop.ledger.com/products/ledger-nano-s?r=0ba5d7199327",
2 : "https://crypto.com/nft/register?utm_source=Brave&utm_medium=cpc&utm_campaign=Brave_NFT_Push_US-en&utm_content=Features",
3 : "https://brave.com/wallet/",
4 : "https://bitcoin.org/en/",
5 : "https://coinmarketcap.com/",
6 : "https://www.youtube.com/",
7 : "https://www.facebook.com/",
8 : "https://www.ledger.com/",
9 : "https://www.amazon.in/Ledger-Nano-Cryptocurrency-Hardware-Wallet/dp/B01J66NF46"
}

browser.get("https://www.google.com")
count = 0
while True:
    count = count +1
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])
    n=random.randint(0,9)
    print(str(count)+")"+"url number ---> "+str(n))
    browser.get(urls[n])
    time.sleep(10)
    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    
    
    



