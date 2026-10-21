import nltk
from nltk.stem import PorterStemmer,LancasterStemmer,SnowballStemmer

text = "Studies studying happily relational relationally running runners easily"
words = text.lower().split()

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

print("Original Words:")
print(words)

print("\nPorter Stemmer:")
for word in words:
    print(word, "->", porter.stem(word))

print("\nLancaster Stemmer:")
for word in words:
    print(word, "->", lancaster.stem(word))

print("\nSnowball Stemmer:")
for word in words:
    print(word, "->", snowball.stem(word))