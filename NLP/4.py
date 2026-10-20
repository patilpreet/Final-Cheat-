import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer

text = "Studies studying happily relational relationally running runners easily"
words = text.lower().split()

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")
lemmatizer = WordNetLemmatizer()

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

print("\nLemmatization:")
for word in words:
    print(word, "->", lemmatizer.lemmatize(word, pos='v'))