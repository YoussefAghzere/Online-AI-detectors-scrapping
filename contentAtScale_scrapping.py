import time
import re

import pyautogui
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import re
import glob

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def readFile(filepath):
    with open(filepath, "r") as df:
        content = df.read()
    return content

def writeFile(filepath, text):
    with open(filepath, "w+") as df:
        try:
            df.write(text)
            return True
        except IOError:
            print(f"!!!!!!!!!!!!!!Can't write in this file : {filepath}!!!!!!!!!!!!!!")


def contentatscale_detector_scrapping(folder): # folder contains subfolders of texts
    driver = webdriver.Firefox()
    driver.get("https://contentatscale.ai/ai-content-detector/")
    wait = WebDriverWait(driver, 300)

    pub_close = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[8]/div/div/button")))
    pub_close.click()

    txt_files = glob.glob(folder + "/**/*.txt")
    dir = "/home/youssef/Desktop/contentAtScale/contentAtScale_scrapping(copy)/Reedsy_Prompts_short_stories_AI_Human_Style/"
    # temp_l = [dir + "Lindsay_Flo/LF1.txt_AI_4663words.txt", dir + "Lindsay_Flo/LF12.txt_AI_4636words.txt", dir + "Lee_Disco/LD11.txt_AI_4930words.txt", dir + "Radius_Havwaala/RH6.txt_AI_4055words.txt", dir + "Brendan_Doyle/BD2.txt_AI_4268words.txt",
    #          dir + "Thom_Brodkin/TB13.txt_AI_4394words.txt", dir + "Sasan_Sedighi/SS4.txt_AI_4445words.txt", dir + "Sasan_Sedighi/SS10.txt_AI_4439words.txt", dir + "Sasan_Sedighi/SS5.txt_AI_4691words.txt", dir + "John_Jenkins/JJ1.txt_AI_4329words.txt"]
    for file in txt_files:
        story = readFile(file)
        # textfield = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/textarea')
        # driver.execute_script("window.scrollTo(0, arguments[0]);", textfield)
        textfield = textarea = driver.execute_script("return document.evaluate('/html/body/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/textarea', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;")

        textfield.clear()
        #textfield.send_keys(story)
        driver.execute_script("arguments[0].value = arguments[1]", textfield, story)
        time.sleep(1)
        check_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/button')
        try:
            driver.execute_script("arguments[0].click();", check_button)
        except:
            print("button not clickable")

        time.sleep(10)
        decision_field = driver.find_element(By.XPATH, '//*[@id="progress"]')
        decision = decision_field.text
        i = 0
        while decision == "0%" and i <= 10:
            time.sleep(4)
            decision = decision_field.text
            i += 1
        with open(file, 'w') as f:
            f.write('')
        f.close()
        with open(file, 'w') as f:
            f.write(decision + ' HUMAN-GENERATED CONTENT')
        f.close()
        print(f"File {file} done")




contentatscale_detector_scrapping("/home/youssef/Desktop/contentAtScale/contentAtScale_scrapping")












"""
driver = webdriver.Firefox()
driver.get("https://contentatscale.ai/ai-content-detector/")

wait = WebDriverWait(driver, 300)
txt_files = ["hey", "hello", "hey", "hello", "hey", "hello", "hey", "hello", "hey", "hello", "hey", "hello", "hey", "hello", "hey", "hello", "hey", "hello" "hey", "hello", "hey", "hello"]
for file in txt_files:
    try:
        pub_close = driver.find_element(By.XPATH, "/html/body/div[8]/div/div/button")
        pub_close.click()
    except NoSuchElementException:
        print("Element not found.")
    story = file
    textfield = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/textarea')
    driver.execute_script("window.scrollTo(0, arguments[0]);", textfield)
    textfield.clear()
    textfield.send_keys(story)
    check_button = driver.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[1]/div[1]/div/div[2]/div[2]/button')
    try:
        driver.execute_script("arguments[0].click();", check_button)
    except:
        print("button not clickable")

    decision_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="progress"]')))
    decision = decision_field.text
    print(decision)
"""
