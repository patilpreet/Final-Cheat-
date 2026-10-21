import re
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize, word_tokenize

text = input("Enter a text: ")
sentences = sent_tokenize(text)
print("Sentences:")
for sentence in sentences:
    print(sentence)

text = input("Enter another text: ")

words_re = re.findall(r'\w+', text)
print("\nWords using re:")
print(words_re)

words_nltk = word_tokenize(text)
print("\nWords using NLTK:")
print(words_nltk)