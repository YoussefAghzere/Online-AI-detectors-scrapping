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


def kazanseo_detector_scrapping(folder): # folder contains subfolders of texts
    driver = webdriver.Firefox()
    driver.get("https://kazanseo.com/detector")
    time.sleep(10)
    driver.get("https://kazanseo.com/detector")
    wait = WebDriverWait(driver, 300)
    textarea = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="text-boxer"]')))
    detect_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[5]/button')))

    txt_files = glob.glob(folder + "/**/*.txt")
    files_done = ['/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4622words_Graphic design.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_6025words_Adventure travel.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5613words_Indigenous cultures.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4913words_History and Archeology.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4844words_Entrepreneurship.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5221words_Subcultures.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5363words_Travel and Exploration.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4660words_Ethics.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5469words_Social movements.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4268words_Team sports.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4678words_Theater.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4640words_Historical figures.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4954words_Sculpture.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4441words_Photography.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4903words_Renewable energy.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5437words_Painting.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5773words_Public health.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4663words_Alternative medicine.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5486words_Human rights.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4930words_Media and Entertainment.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4529words_Fitness trends.txt', '/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4509words_Science and Technology.txt']

    previous_decision = ""
    for file in txt_files:
        if file not in files_done:
            story = readFile(file)
            textarea.clear()
            for s in story.split('.'):
                textarea.send_keys(s)
            time.sleep(1)
            detect_button.click()
            decision_field = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div/div[2]/div[4]/div')))
            decision = decision_normalization(decision_field.text)
            i = 0
            while decision == previous_decision and i < 30:
                time.sleep(1)
                decision = decision_normalization(decision_field.text)
                i += 1
            previous_decision = decision

            with open(file, 'w') as f:
                f.write('')
            f.close()
            with open(file, 'a') as f:
                f.write(decision)
            f.close()
            print(f"File {file} done")





kazanseo_detector_scrapping("/home/youssef/Desktop/online_detectors/KazanSEO/kazanSEO_scrapping/Stories_AI_person_style")





# youssef@gmail.com
