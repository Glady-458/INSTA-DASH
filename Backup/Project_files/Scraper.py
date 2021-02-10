from requests import get
from bs4 import BeautifulSoup
from json import loads
from selenium import webdriver
import time
import pandas
import numpy
import json
# from gui import *

browser = webdriver.Chrome('D:/Web Driver/chromedriver.exe')
browser.minimize_window()
# def cdrive():
    # browser = webdriver.Chrome('D:/Web Driver/chromedriver.exe')
    # browser.minimize_window()
    # username = 'subhojitjana'
    # browser = webdriver.Chrome('D:/Web Driver/chromedriver.exe')
browser.get('https://www.instagram.com/?hl=en')
pagelength=browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
elem = browser.find_element_by_name("username")
elem.clear()
elem.send_keys("")#<--add your username here
elem = browser.find_element_by_name("password")
elem.send_keys("")#<--add your password here
elem.submit()

time.sleep(3)
    # return browser
def insta(uname):
    browser.get("https://www.instagram.com/"+uname+"/?hl=en")
    rr=browser.page_source
    time.sleep(3)
    # browser.quit()
    code = BeautifulSoup(rr)
    scripts = code.select('script')
    if len(scripts[6])==0:
        if len(scripts[7])==0:
            script = scripts[8]
        else:
            script = scripts[7]
    # elif len(scripts[8])==0:
    #     script = scripts[6]
    else:
        script = scripts[6]
    # else:
    # print(scripts[8])
    # c=0
    # for s in scripts:
    #     print('*')
    #     print('*')
    #     print('*')
    #     print(c)
    #     print('************************************************')
    #     c=c+1
    #     print(s)
    # print(len(script))
    content = script.contents[0]
    data_object=content[content.find('{"config"'):-1]
    data_json=loads(data_object)
    user_data=data_json.get('entry_data').get('ProfilePage')[0].get('graphql').get('user')
    return user_data

# D:\Web Driver
#     print("************************************")
#     print(s)
# import time
# from selenium import webdriver
#
# driver = webdriver.Chrome('D:/Web Driver/chromedriver.exe')  # Optional argument, if not specified will search path.
# driver.get('http://www.google.com/');
# time.sleep(50) # Let the user actually see something!
# search_box = driver.find_element_by_name('q')
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# time.sleep(5) # Let the user actually see something!
# driver.quit()
