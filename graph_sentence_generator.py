from graph_data_training import *
from graph import Graph
import functools

MAX_MEMORY = 4

def generate_sentence(graph):
    first_word = get_first_word(graph)
    sentence = [first_word]
    for i in range(0,15):
        sentence = sentence.append(get_next_word(graph, sentence, MAX_MEMORY))
    print_sentence(sentence)

def get_first_word():
    # Are we going to look at words after punctuation?
    # To consider: 2-3 words at start
    return("luxery")

# Memory = sentence generated so far (array)
def get_memory_depth(graph, memory, max_memory):
    max_memory = min(len(memory), max_memory)
    for i in range(0, len(memory)-1):
        curr_word = memory[len(memory) - i - 1].lower()
        next_word = memory[len(memory) - i - 2].lower()
        curr_word_node = graph.get_node(curr_word)
        if curr_word_node == None:
            return 0
        #has_next = functools.reduce(curr_word_node.incoming, lambda edge, has_next : edge.in_node.word == next_word || has_next, False)
        has_next = False
        for edge in curr_word_node.incoming:
            if edge.in_node.word == next_word:
                has_next = True
        if not has_next:
            return min(i + 1, max_memory)
    return min(len(memory), max_memory)

def get_all_next_words(graph, memory, memory_depth):
    #  Return array of edges ?????
    # backtrace to the memory depth nodes... we'll figure the shit of the kinks out later
    # Add memory_depth to the outgoing edgec

# memory: The sentence we've generated so far
# max_memory: How far back we will look when generating the next words
# graph: the graph structure of training data
def get_next_word(graph, memory, max_memory):
    memory_depth_to_search = get_memory_depth(graph, memory, max_memory)
    next_words = get_all_next_words(graph, memory, memory_depth_to_search)



    # "Brian and I like big turkey"
    # -how far back should we actually look/how far back our sentence matches up with prev
    # -get all the next words for how back we actually look

    #  The two of us, we like big turkey

    # MAX_MEMORY = 3
    # we like big turkey lean
    # big turkey is healhy for you
    # sometimes I would say the two of us, we like big turkey big
    #[is, lean, lean, lean, big, big, big]

def print_sentence(sentence_array):
    sentence = ""
    for i in sentence_array:
        sentence += " " + i
    print(sentence)

memory = ["the", "annual", "employee", "awards", "night", "kerfluffel", "at", "dunder", "mifflin"]
max_memory = 4
data = FilesToListOfFileWords(TRAINING_FILES)
graph = create_word_graph(data)
#
# #print(get_node(graph, "the"))
print(get_memory_depth(graph, memory, max_memory))
