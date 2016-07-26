# Python Script To get Meal Pass

#Selenium Imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

#IMAP imports
import smtplib

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

#Grab the Address of the Place
try:
	address = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='meal-reserved']/div[2]/div/div[6]/span[2]")))
	print("Address")
	print(address.text)
	res = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='meal-reserved']/div[2]/div/div[4]/span[2]")))
	print("Resturant")
	print(res.text)
except TimeoutException:
	print("Timeout")
#Send as an email so it can be inputted into Google

serverName = " "
sendFrom = " "
sendTo = " "
Message = address + res
