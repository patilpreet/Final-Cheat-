import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text = input("Enter a sentence: ")
words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)

print("POS Tagged Text:")
print(pos_tags)