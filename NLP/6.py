import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('maxent_ne_chunker')
nltk.download('maxent_ne_chunker_tab')
nltk.download('words')
from nltk import word_tokenize, pos_tag, ne_chunk

text = input("Enter a sentence: ")

tokens = word_tokenize(text)
tagged = pos_tag(tokens)
tree = ne_chunk(tagged)

print("\nNamed Entities:")
for chunk in tree:
    if hasattr(chunk, 'label'):
        entity = " ".join(word for word, tag in chunk)
        print(f"{entity}  ->  {chunk.label()}")