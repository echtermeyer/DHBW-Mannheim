sentence = "the quick brown fox jumps over the lazy dog"

word_lengths = [len(word) for word in sentence.split() if word != "the"]
print(word_lengths)


numbers_7 = [i for i in range(1, 10001) if i%7==0]
print(numbers_7)


teststring = """Find all of the words in a string that are less than 4 letters"""
number_empty = [i for i in teststring if i == " "]
print(len(number_empty))