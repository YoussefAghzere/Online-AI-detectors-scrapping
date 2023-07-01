import time
import re
import undetected_chromedriver as uc

import pyautogui
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import re
import glob

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def split_text(story, chunk_size):
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
    driver.get("https://sapling.ai/ai-content-detector")
    wait = WebDriverWait(driver, 300)
    textarea = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content-editor"]')))
    txt_files = glob.glob(folder + "/**/*.txt")
    files_done = ['/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4622words_Graphic design.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_6025words_Adventure travel.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5613words_Indigenous cultures.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4913words_History and Archeology.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4844words_Entrepreneurship.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5221words_Subcultures.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5363words_Travel and Exploration.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4660words_Ethics.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5469words_Social movements.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4268words_Team sports.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4678words_Theater.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4640words_Historical figures.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4954words_Sculpture.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4441words_Photography.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4903words_Renewable energy.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5437words_Painting.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5773words_Public health.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4663words_Alternative medicine.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5486words_Human rights.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4930words_Media and Entertainment.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4529words_Fitness trends.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4509words_Science and Technology.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4895words_Street art.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_3906words_Public policy.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4512words_Marketing.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5413words_Online education.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4782words_Film.txt']
    files_done = files_done + ['/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4596words_Physics.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4038words_Climate change.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4691words_Performing Arts.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5140words_Sports and Fitness.txt']
    files_done = files_done + ['/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5810words_Cultural tourism.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5294words_Law and Justice.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4969words_Wars.txt']
    files_done = files_done + ['/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4449words_Television.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5313words_Business and Finance.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5152words_Mental health.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4559words_Conservation.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5532words_Gastronomy.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4492words_Dance.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4079words_Language learning.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4742words_World religions.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5858words_Individual sports.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4506words_Environment and Sustainability.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4546words_Biology.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4291words_Spirituality.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5289words_Criminal justice.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5175words_Philosophy and Religion.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4527words_Vocational training.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4733words_Architecture.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4263words_Computer science.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5396words_Culture and Society.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4785words_Comedy.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4698words_Investing.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5294words_Music.txt']
    files_done = files_done + ['/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_4836words_Health and Medicine.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jacob_Brown/JB_AI_5390words_Ancient civilizations.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4587words_Ethics.txt']
    files_done = files_done + ['/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_3789words_Film.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4654words_Individual sports.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4722words_Renewable energy.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4710words_Biology.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4866words_Dance.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4662words_Computer science.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5330words_Entrepreneurship.txt']
    files_done = files_done + ['/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4732words_Physics.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4920words_Travel and Exploration.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4368words_Adventure travel.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4528words_Painting.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5358words_Media and Entertainment.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4248words_Historical figures.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4529words_Subcultures.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4952words_Human rights.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5263words_History and Archeology.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4991words_Public policy.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4399words_Fitness trends.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4578words_Language learning.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5217words_Climate change.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4557words_Television.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4884words_Mental health.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4605words_Sculpture.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4320words_Graphic design.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4469words_Indigenous cultures.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4632words_Photography.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4616words_Comedy.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5210words_Team sports.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4668words_Alternative medicine.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5118words_Wars.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5406words_Criminal justice.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5101words_Philosophy and Religion.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4678words_Cultural tourism.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4539words_Vocational training.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4808words_Marketing.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5053words_World religions.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4693words_Music.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4395words_Ancient civilizations.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4471words_Health and Medicine.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4340words_Spirituality.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4224words_Gastronomy.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4582words_Law and Justice.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4171words_Online education.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4410words_Investing.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4398words_Performing Arts.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4947words_Art and Design.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5181words_Conservation.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4917words_Architecture.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5049words_Business and Finance.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4979words_Social movements.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4522words_Public health.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4846words_Street art.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4773words_Science and Technology.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4808words_Sports and Fitness.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4747words_Environment and Sustainability.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4541words_Culture and Society.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4775words_Theater.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_4856words_Education and Learning.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Brendan_Doyle/BD_AI_5117words_Visual Arts.txt', '/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style/Jeannie_Labelle_Potvin/JL_AI_4087words_Gastronomy.txt']

    for file in txt_files:
        if file not in files_done:
            decisions = []
            story = readFile(file)
            story_chunks = split_text(story, 2000)
            for chunk in story_chunks:
                textarea.clear()
                textarea.send_keys(chunk)
                time.sleep(20)
                decision_field = driver.find_element(By.XPATH, '//*[@id="fake-prob"]')
                decision = decision_field.text
                decisions.append(decision)

            with open(file, 'w') as f:
                f.write('')
            f.close()
            with open(file, 'a') as f:
                for decision in decisions:
                    f.write(decision + '% AI-GENERATED CONTENT\n')
            f.close()
            print(f"File {file} done")


def final_score(folder):
    txt_files_1 = glob.glob(f"{folder}/**/**/*.txt")
    txt_files_2 = glob.glob(f"{folder}/**/*.txt")
    txt_files = txt_files_1 + txt_files_2
    for f in txt_files:
        with open(f, 'r') as file:
            total = 0.0
            count = 0
            for line in file:
                match = re.search(r'^(\d+(?:\.\d+)?)%', line)
                if match:
                    total += float(match.group(1))
                    count += 1

            if count > 0:
                average = total / count
                res = f"{round(average, 2)}% AI-GENERATED CONTENT"
                print(res)
            else:
                res = "No score"
                print(res)
        with open(f, 'w') as file:
            file.write('')
            file.write(res)


# contentatscale_detector_scrapping("/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Stories_AI_person_style")

final_score("/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping_scores")


"""f = "/home/youssef/Desktop/online_detectors/saplingAI/saplingAI_scrapping/Reedsy_Prompts_short_stories_AI_version/Aries_Walker_AI_version/AW10.txt_AI_3332words.txt"
with open(f, 'r') as file:
    total = 0.0
    count = 0
    for line in file:
        match = re.search(r'^(\d+(?:\.\d+)?)%', line)
        if match:
            total += float(match.group(1))
            count += 1

    if count > 0:
        average = total / count
        res = f"{round(average, 2)}% AI-GENERATED CONTENT"
        print(res)
    else:
        res = "No score"
        print(res)
with open(f, 'w') as file:
    file.write('')
    file.write(res)
"""


