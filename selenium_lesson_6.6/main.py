import time
from selenium import webdriver
import json

browser = webdriver.Chrome()
browser.get("https://instagram.com")

with open("instagram.json", mode="r") as file:
    cookies_str = file.read()
    cookies_dict = json.loads(cookies_str)

for cookies in cookies_dict:
    browser.add_cookie(cookies)

browser.get("https://instagram.com")

# time.sleep(30)
#
with open("instagram.json", mode="w") as file:
    file.write(json.dumps(browser.get_cookies()))
    print('Cookie was wrote to file')





# browser = webdriver.Firefox()
# browser.get("https://instagram.com")
# time.sleep(100)
# pickle.dump(browser.get_cookies(), open('session.json', 'wb'))
# print("Куки сохранены")




