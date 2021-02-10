from requests import get
from bs4 import BeautifulSoup
from json import loads
from selenium import webdriver
import time
import pandas
import numpy
import json


username = 'subhojitjana'
browser = webdriver.Chrome('D:/Web Driver/chromedriver.exe')
browser.get('https://www.instagram.com/?hl=en')
pagelength=browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
elem = browser.find_element_by_name("username")
elem.clear()
elem.send_keys("glady_458")
elem = browser.find_element_by_name("password")
elem.send_keys("Suvajit#1997")
elem.submit()
# elem=browser.find_element_by_type("text")
# elem.send_keys('subhojitjana')
# elem.submit()
time.sleep(2)
def insta(uname):
    browser.get("https://www.instagram.com/"+uname+"/?hl=en")
    rr=browser.page_source
    time.sleep(2)
    # browser.quit()
    code = BeautifulSoup(rr)
    scripts = code.select('script')
    # if scripts[6]==None:
    script = scripts[6]
    # else:
    #     script = scripts[6]
    # for s in scripts:
    #     print('*')
    #     print('*')
    #     print('*')
    #     print('*')
    #     print('************************************************')
    #     print(s)
    print(script)
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
