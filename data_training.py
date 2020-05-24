import re
import os
import json

TRAINING_FILES = "./example_data"
OUTPUT_JSON = "trained_data.json"

# Signature: String -> String[]
# REQUIRES: filename is a string to a valid file
# EFFECTS: Returns an array of words and ending punctuation, stored in the same order as in the corresponding file
# Example: if file 'f' consists of "This is a sentence.", returns ['This', 'is', 'a', 'sentenec', '.']
def FileToWords(filename):
    file = open(filename, "r", encoding="utf8")
    contents = file.read().lower()
    file.close()
    contents = re.sub("\.+", " . ", contents)
    contents = re.sub("!", " ! ", contents)
    contents = re.sub("\?", " ? ", contents)
    contents = re.sub(",", " , ", contents)
    contents = re.sub(":", "", contents)
    contents = re.sub("\"", "", contents)
    contents = re.sub("-", "", contents)
    contents = re.sub("{", "", contents)
    contents = re.sub("}", "", contents)
    contents = re.sub("\)", "", contents)
    contents = re.sub("\(", "", contents)
    words = contents.split()
    return(words)


#Signature: String -> String[String []]
#EFFECTS: Returns a list of arrays, where each array is a FileToWords() output from a given file in folder
def FilesToListOfFileWords(folder):
    words = []
    os.chdir(folder)
    for i in os.listdir():
        if "json" not in i.lower() && "tar.gz" not in i.lower():
            words = words + [FileToWords(i)]
    return(words)

#Signature: String[String []] -> Map{String,Map{String,Int}}
#Purpose: Creates a map of words to a mapping of words to occurances seen after the initial word in the given list of files
#Example: [["word","other","!","word","other"], ["!","word"]]-> {"word":{"other": 2}, "other":{"!" : 1}, "!":{"word" : 2}}
def getWordOccurrences(l):
    word_occurences = {}
    for files in l:
        for word_index in range(0,len(files) - 1):
            word = files[word_index]
            next_word = files[word_index + 1]
            next_words = word_occurences.setdefault(word,{})
            next_words.setdefault(next_word,0)
            next_words[next_word] += 1
    return word_occurences

def run_trainer():
    output = json.dumps(getWordOccurrences(FilesToListOfFileWords(TRAINING_FILES)))
    file = open(OUTPUT_JSON,"w+")
    file.write(output)

run_trainer()
