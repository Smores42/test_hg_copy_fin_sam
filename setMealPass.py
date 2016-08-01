# Python Script To get Meal Pass

#Selenium Imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
#IMAP imports
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

driver = webdriver.Firefox()
driver.get("https://www.mealpass.com/")

uName = "samcesario1@gmail.com"
pWord = "sammealpass"

#Click Login
try:
	login_btn = WebDriverWait(driver, 6).until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[1]/div/a")))
	print("Hit Login Button")
	login_btn.click()
except TimeoutException:
	print("TimeOut")
try:
	#Login Actually Necessary
	#Email
	email = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='app']/div[2]/div[1]/div[1]/form/div[2]/div/input")))
	print("Grabbed the Email XPath")
	email.send_keys(uName)
	#Password
	password = WebDriverWait(driver,106).until(EC.presence_of_element_located((By.XPATH,"//*[@id='app']/div[2]/div[1]/div[1]/form/div[3]/div[2]/input")))
	print("Grabbed the Password XPath")
	password.send_keys(pWord)
	#Hit Login Button
	login_btn_1 = WebDriverWait(driver, 6).until(EC.visibility_of_element_located((By.XPATH,"//*[@id='app']/div[2]/div[1]/div[1]/form/button")))
	print("Hit Second Login Button")
	login_btn_1.send_keys("\n")
except TimeoutException:
        print("Timeout")


try:
	# Select the Search bar
	# Type in Choza
	# Wait to Load
	selection = "choza taqueria - madison ave."
	searchBar = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/div[1]/div/mp-filters/div/div/div[1]/div[3]/div[2]/div[1]/input")))
	searchBar.send_keys(selection)
	print("Done Searching")
	searchBarEntr = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='main']/div/div[1]/div/mp-filters/div/div/div[1]/div[3]/div[2]/div[1]/span")))
	searchBarEntr.send_keys("\n")
	print("Hit Enter")
	# Hover over picture
	# Wait for pickuptime box to appear
	hover = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.XPATH,"//*[@id='meal-LQ49kegjMh']/div[1]")))
	hov = ActionChains(driver).move_to_element(hover)
	hov.perform()
	print("Hovering")
	# Select pickup time box to appear and select 12:00 - 12:15 time slot
	picklist = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='meal-LQ49kegjMh']/div[3]/div[4]/button")))
	picklist.click()
	print("Clicked")

	picklistOpt = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='meal-LQ49kegjMh']/div[3]/div[4]/ul/li[3]")))
	picklistOpt.click()
	print("Picked: 12:00 - 12:15")

	# Select Reserve Now
	resvr = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='meal-LQ49kegjMh']/div[3]/div[5]/button")))
	resvr.click()
	print("Reserve Clicked")
	print("Adam! I did it")


except TimeoutException:
	print("TimeOut")


#driver.close()


