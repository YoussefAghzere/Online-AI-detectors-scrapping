import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import glob

def split_text(text, chunk_size):
    # Split text into chunks of chunk_size characters
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
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


def writer_detector_scrapping(folder): # folder contains subfolders of texts
    driver = webdriver.Firefox()
    driver.get("https://writer.com/ai-content-detector/")
    time.sleep(7)
    textfield = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/form/div[2]/textarea")
    reedsy_txt_files = glob.glob(folder + "/**/**/*.txt")
    # reedsy_txt_files = glob.glob(folder + "/**/*.txt")

    for file in reedsy_txt_files:
        decisions = []
        story = readFile(file)
        story_chunks = split_text(story, 1500)
        analyze_text_button = driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div[2]/div[1]/form/button")
        for chunk in story_chunks:
            textfield.clear()
            textfield.send_keys(chunk)
            time.sleep(0.5)
            analyze_text_button.click()
            time.sleep(2)
            decision_field = driver.find_element(By.XPATH, '//*[@id="ai-percentage"]')
            decisions.append(f"{decision_field.text}% HUMAN-GENERATED CONTENT")

        with open(file, 'w') as f:
            f.write('')
        f.close()
        with open(file, 'a') as f:
            for decision in decisions:
                f.write(decision + '\n')
        f.close()   
        print(f"File {file} done")

def final_score(folder):
    txt_files_1 = glob.glob(f"{folder}/**/**/*.txt")
    txt_files_2 = glob.glob(f"{folder}/**/*.txt")
    txt_files = txt_files_1 + txt_files_2
    for f in txt_files:
        with open(f, 'r') as file:
            total = 0
            count = 0
            for line in file:
                match = re.search(r'^(\d+)%', line)
                if match:
                    total += int(match.group(1))
                    count += 1

            if count > 0:
                average = total / count
                res = f"{round(average, 2)}% HUMAN-GENERATED CONTENT"
            else:
                res = "No score"
                print(file)
        with open(f, 'w') as file:
            file.write('')
            file.write(res)

# writer_detector_scrapping("/home/youssef/Desktop/Writer_scrapping")
final_score("/home/youssef/Desktop/Writer_scrapping")
