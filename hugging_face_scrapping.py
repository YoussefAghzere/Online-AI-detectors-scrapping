import requests
import json
import glob

def readFile(filepath):
    with open(filepath, "r") as df:
        content = df.read()
    return content


folder = "/home/youssef/Desktop/huggingFace/huggingFace_scrapping"
file_paths = glob.glob(folder + "/**/*.txt")



for file_path in file_paths:
    story = readFile(file_path)
    response = requests.post("https://piratexx-ai-content-detector.hf.space/run/predict", json={
        "data": [story]
    }).json()

    if "error" in response:
        error_message = response["error"]
        print(f"file {file_path} noooooooooooooooot done")

    elif "data" in response:
        data = response['data']
        decision = data[0][0]['Real']

        with open(file_path, 'w') as f:
            f.write('')
            f.write(str(round(decision * 100, 2)) + '% HUMAN-GENERATED CONTENT')
        print(f"File {file_path} done.")

# No need to close the file explicitly with the "with open" syntax


