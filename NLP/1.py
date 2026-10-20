import nltk
nltk.download('brown')
from nltk.corpus import brown

print("Categories in Brown Corpus:")
print(brown.categories())
print("\nFirst 20 words:")
print(brown.words()[:20])
print("First 20 words from News:")
print(brown.words(categories='news')[:20])
print("\nFirst 20 words from Fiction:")
print(brown.words(categories='fiction')[:20])
print("\nFirst 20 words from Government:")
print(brown.words(categories='government')[:20])
print("\nTotal number of words:")
print(len(brown.words()))
print("\nFirst sentence:")
print(brown.sents()[0])