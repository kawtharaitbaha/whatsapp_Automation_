from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def reply_to_message(contact_name, reply_message):
    driver_path = 'C:\Users\lenovo\Documents\Cours\s6\python avancee\whatsapp_automation\chromedriver-win64.exe'
    driver = webdriver.Chrome(driver_path)

    driver.get('https://web.whatsapp.com')
    time.sleep(15)  # Pause pour scanner le QR code

    search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
    search_box.send_keys(contact_name)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)

    message_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(reply_message)
    message_box.send_keys(Keys.RETURN)

    driver.quit()
