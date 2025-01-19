#! python3
# cmd_line_email.ipynb - Takes an email address and string of text on the command line and then, 
# using selenium, logs into your email account and sends an email of the string to the provided address.

import sys, requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass

if len(sys.argv) != 4: 
    print('Usage: cmd_line_email.py email_address subject message_string')
    sys.exit()

email = sys.argv[1]
subject = sys.argv[2]
message = sys.argv[3]

browser = webdriver.Firefox()
browser.get('https://mail.google.com')

username = input("Enter your email address: ")
password = getpass.getpass("Enter your password: ")

email_elem = browser.find_element(By.ID, 'identifierId')
email_elem.send_keys(username)
email_elem.send_keys(Keys.RETURN)

# Add a wait to ensure the password field is loaded
browser.implicitly_wait(10)

password_elem = browser.find_element(By.NAME, 'password')
password_elem.send_keys(password)
password_elem.send_keys(Keys.RETURN)

compose_elem = browser.find_element(By.XPATH, '//div[text()="Compose"]')
compose_elem.click()

to_elem = browser.find_element(By.NAME, 'to')
to_elem.send_keys(email)

subject_elem = browser.find_element(By.NAME, 'subjectbox')
subject_elem.send_keys(subject)

message_elem = browser.find_element(By.XPATH, '//div[@role="textbox"]')
message_elem.send_keys(message)

send_elem = browser.find_element(By.XPATH, '//div[text()="Send"]')
send_elem.click()

print('Email sent to ' + email)

browser.quit()