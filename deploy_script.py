from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Specify the path using the Service object
service = Service(executable_path="D:/My_Works/vsCode/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.google.com")
#driver.browser("https://google.com")

print('Google opened')