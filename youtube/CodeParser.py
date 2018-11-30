"""
This code parses flatfile data containing timestamps and youtube subtitles
and creates a JSON file from it.
"""

from os import path, listdir
import re
import json


def bad_word_parse():
    with open('bad_words.txt', 'r') as f:
        text = f.read()
        words = text.split(", ")
    with open('bad_word.json', 'w') as f:
        f.write(json.dumps({"offensive_words": words}))


def count_words(text):
    pass


def main():

    dirPath = path.normpath(
        "/home/akshay/Downloads/NLP Project/casey (1)/casey")
    jsonFile = {}
    jsonFile["description"] = "This project attempt to annotate and classify Youtube videos taking into account the content of the video and its composition. While youtube flags content inappropriate for young audiences by requiring viewers to sign in, a lot of youtube content is generally unaudited if the uploader of the video does not flag it so. Also there is no distinction between which content is appropriate for what age groups. We will classify content based the film rating system: G, PG, PG-13 and R. We will also apply a binary classification for classifying clickbait videos."
    jsonFile["corpus"] = []
    for f in listdir(dirPath):
        text = ''
        with open(path.join(dirPath, f)) as file:
            while True:
                lineNo = file.readline().strip()
                if not lineNo:
                    break

                lineTimestamp = file.readline().strip()
                lineText = file.readline().strip()
                blankLine = file.readline().strip()

                if not text:
                    text += lineText
                else:
                    text += ' ' + lineText

        print text

        match = re.search('_(.*)', f)
        fileName = match.groups()[0]
        # print fileName

        jsonFile["corpus"].append({
            'data': text,
            'label': 'U'
        })  

    # print subtitles
    with open('final.json', 'w') as file:
        json.dump(jsonFile, file)


if __name__ == "__main__":
    bad_word_parse()
