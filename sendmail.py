# login
driver.find_element_by_xpath('/html/body/div[4]/section/div[2]/a').click()
time.sleep(3)

email = WebDriverWait(driver, 10 ).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[1]/form/div[1]/div[1]/input")))
time.sleep(2)
# clear input field
email.clear()
# send keys
email.send_keys("brandonkanute@gmail.com")  # input email address here

# password
password = WebDriverWait(driver, 10 ).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[1]/form/div[1]/div[2]/input")))
# clear input field
password.clear()
time.sleep(2)
# send keys
password.send_keys("Brandonkanute1")  # input password here

time.sleep(2)
# click login button
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/main/div/div[1]/form/button")))

# click function
login_btn.click()




