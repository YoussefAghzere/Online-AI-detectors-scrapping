import time
import re
import numpy as np
import pyautogui
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import re
import glob

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def split_text(text, chunk_size):
    text_words = text.split(' ')
    chunks = []
    for i in range(0, len(text_words), chunk_size):
        chunks.append(' '.join(text_words[i: i + chunk_size]))
    return chunks



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
    driver = webdriver.Chrome()
    driver.get("https://crossplag.com/ai-content-detector/")
    time.sleep(20)
    driver.get("https://app.crossplag.com/individual/detector")
    wait = WebDriverWait(driver, 300)
    # txt_files = ["/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping (copy)/Reedsy_Prompts_short_stories/Aries_Walker/AW3.txt",
    #             "/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping (copy)/Reedsy_Prompts_short_stories/Thom_Brodkin/TB4.txt"]

    txt_files = glob.glob(folder + '/**/*.txt')
    files_done = ['/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4622words_Graphic design.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_6025words_Adventure travel.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5613words_Indigenous cultures.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4913words_History and Archeology.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4844words_Entrepreneurship.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5221words_Subcultures.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5363words_Travel and Exploration.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4660words_Ethics.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5469words_Social movements.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4268words_Team sports.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4678words_Theater.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4640words_Historical figures.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4954words_Sculpture.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4441words_Photography.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4903words_Renewable energy.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5437words_Painting.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5773words_Public health.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4663words_Alternative medicine.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5486words_Human rights.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4930words_Media and Entertainment.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4529words_Fitness trends.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4509words_Science and Technology.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4895words_Street art.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_3906words_Public policy.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4512words_Marketing.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5413words_Online education.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4782words_Film.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4596words_Physics.txt', '/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4038words_Climate change.txt']

    for file in txt_files:
        if file not in files_done:
            decisions = []
            story = readFile(file)
            textfield = driver.find_element(By.XPATH, '/html/body/app-root/app-navbar/section/app-text-detector/main/div[2]/div[1]/textarea')

            story_chunks = split_text(story, 2980)
            # driver.execute_script('arguments[0].value = arguments[1]', textfield, story)
            for chunk in story_chunks:
                for s in chunk.split('.'):
                    textfield.send_keys(s + '.')
                time.sleep(1)
                check_button = driver.find_element(By.XPATH, '/html/body/app-root/app-navbar/section/app-text-detector/main/div[2]/div[1]/div[2]/button')
                check_button.click()
                time.sleep(30)
                decision_field = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/app-navbar/section/app-text-detector/main/div[2]/div[2]/div/div[1]/div[1]/div/span')))
                decision = decision_field.text
                decisions.append(decision)
                textfield.clear()
            file = file.replace(' (copy)', '')
            with open(file, 'w') as f:
                f.write('')
            f.close()
            with open(file, 'a') as f:
                for decision in decisions:
                    f.write(decision + ' AI-GENERATED CONTENT')
            f.close()
            print(f"File {file} done ==> {decisions}")



def average_length_of_last_chunk(folder):
    txt_files = glob.glob(folder + "/**/*.txt")
    nb_words = 0
    for file in txt_files:
        story = readFile(file)
        story_last_chunk_nb_words = len(((split_text(story, 2980))[-1]).split(' '))
        nb_words += story_last_chunk_nb_words
    return nb_words / len(txt_files)

def final_score(folder):
    txt_files = glob.glob(folder + "/**/*.txt")
    for file in txt_files:
        txt_file = readFile(file)
        pattern = r'(\d+)% AI-GENERATED CONTENT'
        percentage_rates = re.findall(pattern, txt_file)
        percentage_rates = [int(rate) for rate in percentage_rates]
        for i,rate in enumerate(percentage_rates):
            if rate > 100:
                percentage_rates[i] = 100

        average_rate = 0
        coef = 0
        try:
            for rate in percentage_rates:
                if rate == percentage_rates[-1]:
                    average_rate += rate * 0.5
                    coef += 0.5
                else:
                    average_rate += rate
                    coef += 1
            average_rate = average_rate / coef
            with open(file, 'w') as f:
                f.write('')
                f.write(f'{round(average_rate, 2)}% AI-GENERATED CONTENT')
            f.close()
        except ZeroDivisionError:
            print(f"Error ==> {file}")




# contentatscale_detector_scrapping("/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping/Stories_AI_person_style")

final_score("/home/youssef/Desktop/online_detectors/crossplag/crossplag_scrapping")
