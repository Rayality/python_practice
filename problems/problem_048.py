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
    num = 0
    words = sentence.split()
    for word in words:
        for count,char in enumerate(word):
            if char.isalpha != True:
                word.replace(char, '')
        num = frequency.get(word)
        if num == 0:
            frequency.update({word : 1})
        else:
            frequency.update({word : num})
    return frequency


sentence = "I came, I, saw I learned"
print(count_word_frequencies(sentence))
