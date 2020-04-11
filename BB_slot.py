
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys
import time
import os

def get_bb_slot(url):

    # bring the chromedriver exec to the script path
    driver = webdriver.Chrome(executable_path="./chromedriver")
    driver.get(url)
    print "Please login using OTP and then wait for a while."
    time.sleep(60)

    while 1:
         driver.get(url)
         time.sleep(2)
         print "Trying to find a slot!"
         try:
            driver.find_element_by_xpath("//button[@id = 'checkout']").click()
            time.sleep(5)  # driver take a few sec to update the new url
            src = driver.page_source
            if "checkout" in driver.current_url and not "Unfortunately, we do not have" in src:
                print("Found the slots!")
                for i in range(60):
                    notify("Slots Available!", "Please go and choose the slots!")
                    time.sleep(20)
         except Exception as e:
            print("If this message pops up multiple times, please find the error and create a PR!")
            print(e)
            pass
         print("No Slots found. Will retry again.")
         time.sleep(50)


def notify(title, text):
    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))


get_bb_slot('https://www.bigbasket.com/basket/?ver=1')
