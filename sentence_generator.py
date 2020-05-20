import math
import json
import functools
import random
import os

TRAINING_FILES = "./example_data"
OUTPUT_JSON = "trained_data.json"

def read_training_data():
    os.chdir(TRAINING_FILES)
    file = open(OUTPUT_JSON, "r")
    return json.loads(file.read())

def generate_sentence():
    trained_data = read_training_data()
    first_word = get_first_word(trained_data)
    sentence = first_word[0:1].upper() + first_word[1:]
    last_word = first_word
    sentence_start = False
    for i in range(1, 50):
        random_perc = random_perc = random.random()
        last_word = get_next_word(trained_data[last_word], random_perc)
        if last_word in ".!?,":
            if last_word in ".!?":
                sentence_start = True
            sentence += last_word
        else:
            if sentence_start:
                sentence += " " + last_word[0:1].upper() + last_word[1:]
                sentence_start = False
            else:
                sentence += " " + last_word
            
    return(sentence)

# Retrieves first word for sentence generation
def get_first_word(trained_data):
    punctuation_list = map(lambda punctuation: trained_data[punctuation], [".","!","?"])
    first_words = merge_dicts_list(punctuation_list)
    random_perc = random.random()
    return(get_next_word(first_words, random_perc))

def get_next_word(next_words, random_percentage):
    next_word_count = sum(next_words.values())
    word_to_get = math.floor(random_percentage*next_word_count)
    frequency_count = 0
    for next_word in next_words.keys():
        frequency_count += next_words[next_word]
        if word_to_get < frequency_count:
            return(next_word)

def merge_dicts_list(list_of_dicts):
    return(functools.reduce(merge_dicts, list_of_dicts, {}))

def merge_dicts(dict1, dict2):
    merge_dict = dict1.copy()
    for key in dict2.keys():
        merge_dict.setdefault(key,0)
        merge_dict[key] += dict2[key]
    return(merge_dict)

print(generate_sentence())
