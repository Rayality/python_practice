# Write a function that meets these requirements.
#
# Name:       count_word_frequencies
# Parameters: sentence, a string
# Returns:    a dictionary whose keys are the words in the
#             sentence and their values are the number of
#             times that word has appeared in the sentence
#
# The sentence will contain now punctuation.
#
# This is "case sensitive". That means the word "Table" and "table"
# are considered different words.
#
# Examples:
#    * sentence: "I came I saw I learned"
#      result:   {"I": 3, "came": 1, "saw": 1, "learned": 1}
#    * sentence: "Hello Hello Hello"
#      result:   {"Hello": 3}


def count_word_frequencies(sentence):
    frequency = {}
    words = sentence.split()
    for word in words:
        frequency[word] = frequency.setdefault(word, 0) + 1
    return frequency


def most_frequent(lyrics):
    frequency = {}
    minimum_occurance = 10
    translate_table = str.maketrans("", "", "(),'")
    words = lyrics.lower().translate(translate_table).split()
    for word in words:
        frequency[word] = frequency.setdefault(word, 0) + 1

    return {k: v for (k, v) in frequency.items() if v > minimum_occurance}
