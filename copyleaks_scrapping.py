import time
import re
import undetected_chromedriver as uc
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
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


def contentatscale_detector_scrapping(folder): # folder contains subfolders of texts
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-cookies')
    options.add_argument('--incognito')
    driver = uc.Chrome(options=options)
    driver.get("https://copyleaks.com/ai-content-detector")
    wait = WebDriverWait(driver, 300)

    txt_files = glob.glob(folder + "/**/*.txt")
    files_done = ['/home/youssef/Desktop/online_detectors/copyleaks/copyleaks_scrapping/Reedsy_Prompts_short_stories/Jacob_Brown/JB1.txt', '/home/youssef/Desktop/online_detectors/copyleaks/copyleaks_scrapping/Reedsy_Prompts_short_stories/Jacob_Brown/JB6.txt']
    for file in txt_files:
        if file not in files_done:
            story = readFile(file)
            story_chunks = split_text(story, 24000)
            decisions = []

            iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="ai-content-detector"]')))
            # textarea = driver.find_element(By.TAG_NAME, 'textarea')
            textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'textarea')))
            # textarea.clear()
            check_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-scan-inline-widget-layout/app-submit-ai-scan-text-page/div/div[1]/div[3]/div/cls-spinner-button/button')))

            for chunk in story_chunks:
                for s in chunk.split('.'):
                    textarea.send_keys(s + '.')
                check_button.click()
                decision = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="website-container"]/app-scan-inline-widget-layout/app-submit-ai-scan-text-page/div/div[1]/div[5]/div/div[1]')))
                decisions.append(decision.text)
                print(decision.text)
                clear_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-scan-inline-widget-layout/app-submit-ai-scan-text-page/div/div[1]/div[4]/button')))
                clear_button.click()

            driver.switch_to.default_content()

            with open(file, 'w') as f:
                f.write('')
            f.close()
            with open(file, 'a') as f:
                for decision in decisions:
                    f.write(decision + '\n')
            f.close()
            print(f"File {file} done")




contentatscale_detector_scrapping("/home/youssef/Desktop/online_detectors/copyleaks/copyleaks_scrapping/Reedsy_Prompts_short_stories")






"""
textpath = '/home/youssef/Desktop/copyleaks/copyleaks_scrapping/Reedsy_Prompts_short_stories_AI_Person_style/Sasan_Sedighi/SS3.txt_AI_11780words.txt'
story = readFile(textpath)
story_chunks = split_text(story, 24000)

options = webdriver.ChromeOptions()
options.add_argument('--disable-cookies')
options.add_argument('--incognito')
driver = uc.Chrome(options=options)
driver.get("https://copyleaks.com/ai-content-detector")
wait = WebDriverWait(driver, 300)

# cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/button')))
# cookies_button.click()

# Switch to the iframe
iframe = wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//*[@id="ai-content-detector"]')))
textarea = driver.find_element(By.TAG_NAME, 'textarea')
check_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-scan-inline-widget-layout/app-submit-ai-scan-text-page/div/div[1]/div[3]/div/cls-spinner-button/button')))

for chunk in story_chunks:
    textarea = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'textarea')))
    for s in chunk.split('.'):
        textarea.send_keys(s + '.')
    time.sleep(2)
    check_button.click()
    decision = wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/app-root/div/app-scan-inline-widget-layout/app-submit-ai-scan-text-page/div/div[1]/div[5]/div/div[1]/span')))
    print(decision.text)
    clear_button = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/app-root/div/app-scan-inline-widget-layout/app-submit-ai-scan-text-page/div/div[1]/div[4]/button')))
    clear_button.click()
# driver.execute_script("arguments[0].value = arguments[1]", textarea, story_chunks[0])


#textarea.clear()
time.sleep(500)
# textarea.send_keys(story)

# Switch back to the default content (outside the iframe)
driver.switch_to.default_content()
"""
