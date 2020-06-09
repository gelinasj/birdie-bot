import re
import os
import json
from tweeter.graph import Graph

UNPACK_COMPRESSED_DATA = 'tar zxvf data.tar.gz'
TRAINING_FILES = "./tweeter/example_data"
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

#Signature: String -> String[]
#EFFECTS: Returns an array of words
# Input is a file/string of multiple words
def FilesToListOfFileWords(folder):
    words = []
    os.chdir(folder)
    for i in os.listdir():
        if "json" not in i.lower():
            words = words + FileToWords(i)
    return(words)

def create_word_graph(data):
    #Make first node with first word
    graph = Graph()
    last_word = graph.create_node_if_dne(data[0])
    for i in range(1, len(data)):
        curr_word = graph.create_node_if_dne(data[i])
        graph.create_edge(last_word, i, curr_word)
        last_word = curr_word
    return(graph)
