from graph_data_training import *
from graph import Graph
import functools
import random
import itertools

MAX_MEMORY = 3

# memory = sentence generated so far (array)
# max_memory = Pre-determined depth of interest for matching sentences
# Returns how far back we are able to look for our matching phrases
# Returns the minimum value of max_memory and the maximum depth of matches in our sentence
def get_memory_depth(graph, memory, max_memory):
    max_memory = min(len(memory), max_memory)
    for i in range(0, len(memory)-1):
        curr_word = memory[len(memory) - i - 1].lower()
        next_word = memory[len(memory) - i - 2].lower()
        curr_word_node = graph.get_node(curr_word)
        # has_next = functools.reduce(curr_word_node.incoming, lambda edge, has_next : (edge.in_node.word == next_word) or has_next, False)
        has_next = False
        for edge in curr_word_node.incoming:
            if edge.in_node.word == next_word:
                has_next = True
        if not has_next:
            return min(i + 1, max_memory)
    return min(len(memory), max_memory)

# Gets all the potential next words that match of phrases that match to the
# degree of the memory depth. Note if the memory_depth is 4 but a phrase only
# matches to a degree of 2, then this phrase is not used for the next words
def get_all_next_words(graph, memory, memory_depth):
    potential_edges = graph.get_node(memory[len(memory) - 1]).outgoing
    next_words = []
    # Consider all potential next edges, filter by match length
    for potential_edge in potential_edges:
        next_word = potential_edge.out_node.word
        # save edge_count of potential_edge
        potential_edge_count = potential_edge.edge_count
        match_depth = 0
        for i in range(0, memory_depth):
            curr_word_memory = memory[len(memory) - i - 1].lower()
            check_word = graph.get_edge(potential_edge_count - i).in_node.word
            if check_word != curr_word_memory:
                break
            match_depth += 1
        # Add to candidate words here
        if match_depth == memory_depth:
            next_words.append(next_word)
        # next_words = next_words + ([next_word] * match_depth * match_depth * match_depth)
    return(next_words)

# memory: The sentence we've generated so far
# max_memory: How far back we will look when generating the next words
# graph: the graph structure of training data
def get_next_word(graph, memory, max_memory):
    memory_depth_to_search = get_memory_depth(graph, memory, MAX_MEMORY)
    next_words = get_all_next_words(graph, memory, memory_depth_to_search)
    # Choose a word at random
    return(next_words[random.randint(0, len(next_words) - 1)])

def generate_sentence(graph):
    sentence = get_starting_memory(graph)
    for i in range(0,15):
        sentence.append(get_next_word(graph, sentence, MAX_MEMORY))
    return(sentence)

def get_starting_memory(graph):
    # Are we going to look at words after punctuation?
    # To consider: 2-3 words at start
    return(["people", "say"])

# Prints the array of words into a sentence
def print_sentence(sentence_array):
    sentence = ""
    for word in sentence_array:
        if word in ",.?!":
            sentence += word
        else:
            sentence += " " + word
    print(sentence)

def driver():
    data = FilesToListOfFileWords(TRAINING_FILES)
    graph = create_word_graph(data)
    print_sentence(generate_sentence(graph))

driver()
