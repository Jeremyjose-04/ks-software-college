import time 
from selenium import webdriver
browser= webdriver.chrome()
browser.get("https://www.google.com")
time.sleep(5)
browser.maximize_window()
time.sleep(5)
browser.minimize_window()
time.sleep(5)
browser.quit()