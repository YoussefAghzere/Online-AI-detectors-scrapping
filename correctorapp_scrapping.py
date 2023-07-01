import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import glob
import undetected_chromedriver as uc
from selenium.webdriver.common.action_chains import ActionChains
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


def writer_detector_scrapping(folder): # folder contains subfolders of texts
    driver = uc.Chrome()
    driver.get("https://corrector.app/ai-content-detector/")
    time.sleep(1)
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
            time.sleep(60)
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

# writer_detector_scrapping("/home/youssef/Desktop/Writer_scrapping")

ai_text = """Secondly, Mond recognizes the limitations of happiness. In the novel, the government encourages the citizens to pursue pleasure and happiness at all times, but Mond understands that this is not a sustainable or fulfilling way of life. He acknowledges that true happiness cannot be found through constant pleasure and that individuals need to find meaning and purpose in their lives. This is evident in his statement, "ending is better than mending. The more stitches, the less riches." This quote shows that Mond recognizes that true happiness cannot be found in constant pleasure, but rather in finding meaning in one's life.

Lastly, Mond believes in individual freedom. Despite his role in controlling society, he recognizes that individuals have the right to make their own choices and live their lives as they see fit. This is evident in his decision to provide a reservation for those who do not want to conform to the rules of society. This shows that Mond understands that individuals should have the freedom to live their lives as they choose, even if it means going against the norms of society.

In conclusion, Mustapha Mond, the World Controller in Aldous Huxley's "Brave New World," should be viewed positively for his efforts to maintain stability in society, his recognition of the limitations of happiness and his belief in individual freedom. Although his methods are controversial, they are necessary to maintain the balance of society. His recognition of the limitations of happiness and his belief in individual freedom also show that he is a nuanced and thoughtful leader who understands the complexity of human nature."""



driver = webdriver.Firefox()
# driver.get("https://corrector.app/ai-content-detector/")
time.sleep(1)
wait = WebDriverWait(driver, 300)

story = readFile('/home/youssef/Desktop/correctorAPP/correctorapp_scrapping/Reedsy_Prompts_short_stories_AI_version/Aries_Walker_AI_version/AW1_AI_3285words.txt')
story_chunks = split_text(story, 780)
# story_chunks[0] = ai_text
for chunk in story_chunks:
    driver.get("https://corrector.app/ai-content-detector/")
    cookies_node = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="ez-cookie-dialog-wrapper"]')))
    driver.execute_script('arguments[0].remove();', cookies_node)
    textarea = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="checktext"]')))
    time.sleep(2)
# driver.execute_script('arguments[0].value = arguments[1];', textarea, story)
    for w in chunk.split('.'):
        textarea.send_keys(w + '.')
    check_button = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="correct"]')))
    actions = ActionChains(driver)
    actions.move_to_element(check_button).click().perform()
    # driver.execute_script('arguments[0].click();', check_button)
    time.sleep(60)
    decision = driver.find_element(By.XPATH, '/html/body/div[5]/div/div/main/article/div/div/div[1]/table/tbody/tr/td[1]/span')
    print(decision.text)



time.sleep(300)
