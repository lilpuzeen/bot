from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome("/Users/armantovmasyan/PycharmProjects/bot/chromedriver", options=options)
driver.get("https://mail.google.com/mail/u/0/#inbox")
time.sleep(5)
print("Done!")
driver.quit()
