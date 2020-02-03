import time 
from selenium import webdriver
browser = webdriver.Firefox()
browser.get('http://username:password@hostname//new/#system')
time.sleep(10)
element = browser.find_element_by_css_selector(".leftcol:nth-child(1) button")
element.click()
assert browser.switch_to.alert.text == "Are you sure you want to reboot?"
browser.switch_to.alert.accept()
