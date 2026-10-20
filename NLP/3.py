import re
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize, word_tokenize

text = "Natural Language Processing is a part of AI. It helps computers understand human language. NLP is used in chatbots."
sentences = sent_tokenize(text)
print("Sentences:")
for sentence in sentences:
    print(sentence)

text = "Natural Language Processing is very interesting."

words_re = re.findall(r'\w+', text)
print("\nWords using re:")
print(words_re)

words_nltk = word_tokenize(text)
print("\nWords using NLTK:")
print(words_nltk)