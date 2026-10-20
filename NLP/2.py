import nltk
nltk.download('treebank')
from nltk.corpus import treebank

print("First 20 words:")
print(treebank.words()[:20])

print("\nFirst sentence:")
print(treebank.sents()[0])

print("\nTotal number of words:")
print(len(treebank.words()))

print("\nFirst 20 POS-tagged words:")
print(treebank.tagged_words()[:20])