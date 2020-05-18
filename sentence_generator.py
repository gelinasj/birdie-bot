import data_training
import json

def read_training_data():
    file = open(data_training.OUTPUT_JSON, "r")
    return json.loads(file.read())


def generate_sentence():
    trained_data = read_training_data()


generate_sentence()
