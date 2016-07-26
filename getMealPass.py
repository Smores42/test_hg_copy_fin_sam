# Python Script To get Meal Pass

#Selenium Imports
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

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

#Grab the Address of the Place
try:
	address = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='meal-reserved']/div[2]/div/div[6]/span[2]")))
	print("Address")
	print(address.text)
	res = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='meal-reserved']/div[2]/div/div[4]/span[2]")))
	print("Resturant")
	print(res.text)
	time = WebDriverWait(driver, 6).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='meal-reserved']/div[2]/div/div[5]/span[2]")))
except TimeoutException:
	print("Timeout")
#Send as an email so it can be inputted into Google

msg = MIMEMultipart()
msg['Subject'] = 'Meal Pass Google Card'
msg['From'] = 'SamDummy12@gmail.com'
msg['To']  = "samcesario1@gmail.com"
#msg.add_header('Content-Type','text/html')

#Mes = time.text + address.text + res.text
#print(Mes)
Message1 = "<html><body>Meal Pass Reservation <br />Order for: Sam Cesario<br/>Event:Meal Pass Event"
Message2 = Message1 + " <br/>When:" + time.text
Message3 = Message2 + " <br/>Venue:" + res.text

Message5 = Message3 + ("<script type='application/ld+json'>" +
"{" +
  "@context': 'http://schema.org',"+
  "@type': 'EventReservation', "+
  "reservationNumber': 'E123456789',"+
  "reservationStatus': 'http://schema.org/Confirmed',"+
  "underName': {"+
    "@type': 'Person',"+
    "name': 'John Smith'"+
  "},"+
  "reservationFor': {"+
    "@type': 'Event',"+
    "name': 'Foo Fighters Concert',"+
    "startDate': '2017-03-06T19:30:00-08:00',"+
    "location': {"+
      "@type': 'Place',"+
      "name': 'AT&T Park',"+
      "address': {"+
        "@type': 'PostalAddress',"+
        "streetAddress': '24 Willie Mays Plaza',"+
        "addressLocality': 'San Francisco',"+
        "addressRegion': 'CA',"+
        "postalCode': '94107',"+
        "addressCountry': 'US'"+
   "   }"+
  "  }"+
 " }"+
"}"+
"</script></body></html>")



msg.attach(MIMEText(Message5,'html'))
#Connect to SMTP
smtpO = smtplib.SMTP('smtp.gmail.com:587')
print("Connected")
smtpO.ehlo()
smtpO.starttls()
smtpO.ehlo()
smtpO.login('SamDummy12@gmail.com','samgoogle')
smtpO.sendmail(msg['From'],msg['To'],msg.as_string())
smtpO.quit()

