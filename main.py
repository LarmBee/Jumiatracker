import time
import smtplib
import csv
import selenium
import pandas as pd


from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from sys import exit
# my lists

myinfo = []
items = []
prces = []
lnks = []

# This might bring up an error so please make sure you have your web driver path correct
# headless options
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")

# driver = webdriver.Chrome(executable_path=r'C:\chromedriver_win32\chromedriver.exe', chrome_options=options)
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)

def run():
    # open our website
    driver.get("https://www.jumia.co.ke/")
    print("Starting Script...")
    # product
    search_term = input("What product are you searching for : ")

    # https://www.jumia.co.ke/oppo/?price=400-20000
    # get search box
    search_box = driver.find_element_by_xpath("/html/body/div[1]/header/section/div/form/div/input")
    search_box.clear()
    search_box.send_keys(search_term)
    search_box.send_keys(Keys.ENTER)
    print(f"Looking for {search_term} ...")
    time.sleep(1)

    # price range
    my_prices = input("What is the max price for what you require : ")
    driver.get(driver.current_url + '&price=-' + my_prices)
    # no of products
    # use web driver wait to wait for elements to load in site
    time.sleep(3)
    results = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/main/div[2]/div[3]/section/header/div[2]/p')))
    print(f'There are {results.text} on the {search_term} item...')
    time.sleep(2)

    # PRODUCT LIST

    # Get product titles
    Title = driver.find_element_by_xpath("/html/body/div[1]/main/div[2]/div[3]/section/div[1]/article[1]/a/div[2]/h3")
    Title_text = Title.get_attribute("innerHTML").splitlines()[0]
    # print titles
    # print(Title_text)

    # get price
    actual_price = driver.find_element_by_class_name("old")
    actual_price = actual_price.text
    discounted_price = driver.find_element_by_class_name("prc")
    discounted_price = discounted_price.text
    # print(f"Actual Price : " + actual_price)
    # print(f"Selling currently at  : " + discounted_price)

    # loop trial
    products = driver.find_elements_by_class_name("name")
    prices = driver.find_elements_by_class_name("prc")
    link = driver.find_elements_by_class_name("core")
    for elem in link:
        links = (elem.get_attribute("href"))
        lnks.append(links)
    for loop in products:
        text = loop.text
        items.append(text)
        # print(text)
    for pricing in prices:
        text2 = pricing.text
        prces.append(text2)
        # print(text2)
    # print format
    # print('%s ,%s, %s' % (items , prces, lnks))
    q = [' '.join(x) for x in zip(items, prces, lnks)]

    # print out all products and prices side by side
    # print(q)
    # information containing price and title
    info = ( discounted_price)
    myinfo.append(info)

    # write to excel workbook
    df = pd.DataFrame(q)
    writer = pd.ExcelWriter('test.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='products', index=False)
    writer.save()

    print("Product lists have been saved to excel file please open and save the data")
    email = 12
    # !! ---EMAIL SECTION ---!!
    if email > 1200000:

        # login credentials
        login = 'jumiaupdate@outlook.com'
        password = '123@jumia'
        # Specify the sender’s and receiver’s email addresses:
        sender = 'jumiaupdate@outlook.com'
        receiver = 'brandonkanute@gmail.com'

        # #
        message = f"""\
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
        print("Recommended price still not met . No email sent ")

    # Load Excel file

    prompt = input("would you like to run the program ? (yes or no) :")
    while prompt == "yes":
        print('Please open test.xlsx file and save current item as python does not auto save before rerunning')
        print('The current results will be overwritten every time you run')
        run()
    else:
        exit()


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    run()
