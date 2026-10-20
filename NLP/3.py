import re
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize, word_tokenize

text = input("Enter text: ")

print("\n--- Sentence Segmentation ---")
print("Using NLTK:")
for i, s in enumerate(sent_tokenize(text), 1):
    print(i, s)

print("\nUsing re:")
sentences = re.split(r'(?<=[.!?])\s+', text.strip())
for i, s in enumerate(sentences, 1):
    print(i, s)

print("\n--- Word Segmentation ---")
print("Using re:")
print(re.findall(r'\b\w+\b', text))

print("\nUsing NLTK:")
print(word_tokenize(text))