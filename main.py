import time
import smtplib
import csv
import selenium
import urllib.request
import json


from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

DIRECTORY = 'reports'
myinfo = []

# This might bring up an error so please make sure you have your web driver path correct
driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")

# open our website
driver.get("https://www.jumia.co.ke/")
print("Starting Script...")
# product
search_term = "Microwave oven"
# price range
price = 0 - 12000
# get search box
search_box = driver.find_element_by_xpath("/html/body/div[1]/header/section/div/form/div/input")
search_box.clear()
search_box.send_keys(search_term)
search_box.send_keys(Keys.ENTER)
print(f"Looking for {search_term} ...")
time.sleep(1)


# no of products
results = driver.find_element_by_xpath('/html/body/div[1]/main/div[2]/div[3]/section/header/div[2]/p')
print(f'There are {results.text} on the {search_term} item...')
time.sleep(2)

# PRODUCT LIST

# Get product titles
Title = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[3]/section/div[1]/article[1]/a/div[2]/h3")
Title_text = Title.get_attribute("innerHTML").splitlines()[0]
print(Title_text)


# get price
raw_Price = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[3]/section/div[1]/article[1]/a/div[2]/div[2]/div[1]")
price = (raw_Price.text)
discounted_price = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[3]/section/div[1]/article[1]/a/div[2]/div[1]")
discount = (discounted_price.text)
print(f"Actual Price : " + price)
print(f"Selling currently at  : " + discount)

# information containing price and title
info = (price, discount)
myinfo.append(info)

# write to excel workbook

# !! ---EMAIL SECTION ---!!
if price > 1200000:

    # login credentials
    login = 'jumiaupdate@outlook.com'
    password = '123@jumia'
    # Specify the sender’s and receiver’s email addresses:
    sender = 'jumiaupdate@outlook.com'
    receiver = 'brandonkanute@gmail.com'

    # #
    message =  f"""\
    Subject : Your monitored product {search_term}
    To : {receiver}
    From :{sender}
    
    Your product {search_term} is at recommended price you can log into jumia and buy it 
    now . This is an automated message please do not reply.
    
    """

    server = smtplib.SMTP('smtp-mail.outlook.com', 587)
    server.starttls()
    server.login(login, password)
    print('Sent')
    server.sendmail(sender, receiver, message)
    print("Email has been sent to", receiver)



