import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

text = input("Enter a sentence: ")
words = word_tokenize(text)
tagged_words = pos_tag(words)
named_entities = ne_chunk(tagged_words)

print("Named Entities:")
print(named_entities)