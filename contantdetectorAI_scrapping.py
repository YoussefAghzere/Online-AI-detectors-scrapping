import time
import re
import undetected_chromedriver as uc
import math
import pyautogui
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import re
import glob

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def decision_normalization(decision):
    match = re.search(r'\d+\.\d+', decision)
    if match:
        rate = float(match.group())
        real_or_fake = (decision.split(' ')[-1])
        if real_or_fake == 'Real':
            pass
        else :
            rate = round(100 - rate, 2)
    else:
        rate = ""

    return f"{rate}% HUMAN-GENERATED CONTENT\n"


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


def contentdetectorai_detector_scrapping(folder): # folder contains subfolders of texts
    driver = uc.Chrome()
    driver.get("https://contentdetector.ai/")
    time.sleep(2)
    wait = WebDriverWait(driver, 300)
    textarea = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div')))
    analyze_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div[2]/div[1]/div[2]/button')))

    txt_files = glob.glob(folder + "/**/*.txt")
    files_done = []

    for file in txt_files:
        if file not in files_done:
            textarea.clear()
            story = readFile(file)
            for chunk in story.split('.'):
                textarea.send_keys(chunk + '.')
            analyze_button.click()

            decision_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div[2]/div[2]/div[1]/p[2]/span/b')))
            decision = decision_field.text

            with open(file, 'w') as f:
                f.write('')
            f.close()
            with open(file, 'a') as f:
                f.write(decision)
            f.close()
            print(f"File {file} done")




contentdetectorai_detector_scrapping("/home/youssef/Desktop/online_detectors/contentdetectorAI/contantdetectorAI_scrapping/Reedsy_Prompts_short_stories_AI_Person_style")







"""driver = webdriver.Chrome()
driver.get("https://contentdetector.ai/")
time.sleep(2)
wait = WebDriverWait(driver, 300)
textarea = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div/div')))
analyze_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div[2]/div[1]/div[2]/button')))
txt_files = ['/home/youssef/Desktop/online_detectors/contentdetectorAI/contantdetectorAI_scrapping/Reedsy_Prompts_short_stories_AI_version/Aries_Walker_AI_version/AW10.txt_AI_3332words.txt', '/home/youssef/Desktop/online_detectors/contentdetectorAI/contantdetectorAI_scrapping/Reedsy_Prompts_short_stories/Aries_Walker/AW2.txt']
for file in txt_files:
    story = readFile(file)

    # driver.execute_script('arguments[0].innerText = arguments[1]', textarea, story)
    textarea.send_keys(story)
    for chunk in story.split('.'):
        textarea.send_keys(chunk + '.')
    analyze_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/main/div[1]/div[2]/div[1]/div[2]/button')))
    analyze_button.click()
    time.sleep(300)
    decision_field = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[1]/div[2]/div[2]/div[1]/p[2]/span/b')))
    print(decision_field.text + ' AI-GENERATED CONTENT\n')
    # textarea.clear()
    clear_button = driver.find_element(By.XPATH, '/html/body/div/main/div[1]/div[2]/div[1]/div[1]/div[3]/div[2]/span[2]')
    clear_button.click()
"""
