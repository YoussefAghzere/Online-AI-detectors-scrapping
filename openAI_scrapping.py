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
import numpy as np

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def split_story(story, chunk_size):
    # Split the story into words
    words = story.split()

    chunks = []
    current_chunk = ''

    for word in words:
        # If adding the word to the current chunk would make it too long, start a new chunk
        if len(current_chunk) + len(word) + 1 > chunk_size:
            chunks.append(current_chunk.strip())
            current_chunk = ''

        # Add the word to the current chunk, along with a space
        current_chunk += word + ' '

    # Add the last chunk to the list of chunks
    if current_chunk:
        chunks.append(current_chunk.strip())

    # Combine adjacent chunks if they are too short
    final_chunks = []
    current_chunk = ''
    for chunk in chunks:
        if len(current_chunk) + len(chunk) + 1 <= chunk_size:
            current_chunk += chunk + ' '
        else:
            if current_chunk:
                final_chunks.append(current_chunk.strip())
            current_chunk = chunk
    if current_chunk:
        final_chunks.append(current_chunk.strip())

    return final_chunks

def split_text(story, chunk_size, chunk_minimum_size):
    if (len(story) % chunk_size) > chunk_minimum_size:
        return split_story(story, chunk_size)
    else:
        new_chunk_size = (len(story) // math.ceil(len(story) / chunk_size)) + 1
        return split_story(story, new_chunk_size)


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


def openai_detector_scrapping(folder): # folder contains subfolders of texts
    driver = webdriver.Chrome()
    driver.get("https://platform.openai.com/ai-text-classifier")
    time.sleep(20)
    wait = WebDriverWait(driver, 300)
    textarea = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[3]/textarea')))
    submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[5]/button[1]')))
    txt_files = glob.glob(folder + "/**/*.txt")
    files_done = []
    for file in txt_files:
        if file not in files_done:
            decisions = []
            story = readFile(file)
            story_chunks = split_text(story, 15000, 10000)
            for chunk in story_chunks:
                textarea.clear()
                for s in chunk.split('.'):
                    textarea.send_keys(s + '.')
                submit_button.click()
                time.sleep(7)
                decision_field = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div/div[2]/div[6]/span/b')
                decision = decision_field.text
                decisions.append(decision)

            with open(file, 'w') as f:
                f.write('')
            f.close()
            with open(file, 'a') as f:
                for decision in decisions:
                    f.write(decision + ' AI-GENERATED CONTENT\n')
            f.close()
            print(f"File {file} done")



def replace_content(filename):
    scores = []
    with open(filename, 'r') as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if "unlikely AI-GENERATED CONTENT\n" == line:
            scores.append(25)
        elif "unclear if it is AI-GENERATED CONTENT\n" == line:
            scores.append(50)
        elif "possibly AI-GENERATED CONTENT\n" == line:
            scores.append(75)
        elif "very unlikely AI-GENERATED CONTENT\n" == line:
            scores.append(0)
        elif "likely AI-GENERATED CONTENT\n" == line:
            scores.append(100)

    average_score = np.mean(scores)

    with open(filename, 'w') as f:
        f.write('')
        f.write(f"{average_score}% AI-GENERATED CONTENT")
    f.close()



def final_score(folder):
    txt_files_1 = glob.glob(f"{folder}/**/**/*.txt")
    txt_files_2 = glob.glob(f"{folder}/**/*.txt")
    txt_files = txt_files_1 + txt_files_2
    for file in txt_files:
        replace_content(file)

# openai_detector_scrapping("/home/youssef/Desktop/online_detectors/openAI/openAI_scrapping")
final_score("/home/youssef/Desktop/online_detectors/openAI/openAI_scrapping_scores")




# youssefaghzere05@gmail.com
