import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize

sentence = input("Enter a sentence: ")

tokens = word_tokenize(sentence)
tagged = nltk.pos_tag(tokens)

print("\nWord\t\tPOS Tag")
for word, tag in tagged:
    print(f"{word}\t\t{tag}")