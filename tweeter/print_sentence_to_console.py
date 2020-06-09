# file = open("propernouns", "r")
# proper_nouns = json.loads(file.read())
# proper_nouns_lower = ["word"] * len(proper_nouns)
# for i in range(0, len(proper_nouns)):
#     proper_nouns_lower[i] = proper_nouns[i].lower()

import tweeter.graph_sentence_generator

print(generate_sentence_string())
