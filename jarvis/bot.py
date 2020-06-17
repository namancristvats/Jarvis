from selenium import webdriver
import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
global chrome


# print("enter username")
# username=input()
# print("enter password")
# password=input()
# print("enter url")
def path():
    global chrome
    chrome=webdriver.Chrome(executable_path="C:\\Windows\\chromedriver")
def Url_name():
    chrome.get("https://www.instagram.com")
    time.sleep(4)
# path()
# Url_name()
def login(username,password):
    usern=chrome.find_element_by_name("username")
    usern.send_keys(username)
    passw=chrome.find_element_by_name("password")
    passw.send_keys(password)
    passw.submit()

