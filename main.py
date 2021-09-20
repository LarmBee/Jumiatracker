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
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

DIRECTORY = 'reports'
myinfo = []

# This might bring up an error so please make sure you have your web driver path correct
# headless options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe", chrome_options=options)

# open our website
driver.get("https://www.jumia.co.ke/")

print("Starting Script...")
# product
search_term = "Sound Bars"
# price range
price = 0 - 12000
my_price = 120000
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
actual_Price = driver.find_element_by_class_name("old")
actual_Price = actual_Price.text
discounted_price = driver.find_element_by_class_name("prc")
discounted_price = discounted_price.text
print(f"Actual Price : " + actual_Price)
print(f"Selling currently at  : " + discounted_price)


# loop trial
items = []
products = driver.find_elements_by_class_name("name")
prices = driver.find_elements_by_class_name("prc")
for loop in products:
    text = loop.text
    items.append(text)
   # print(text)
for pricing in prices:
    text2 = pricing.text
    items.append(text2 )
   #  print(text2)

    print(items)
# information containing price and title
info = (price, discounted_price)
myinfo.append(info)

# write to excel workbook

# !! ---EMAIL SECTION ---!!
if my_price > 1200000:

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

else:
    print("Reccomended price still not met . No email sent ")
