import string
import nltk
nltk.data.path.append("./nltk_data")  # Optional if you want to specify custom data folder
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

with open("sample.txt", "r") as file:
    text = file.read()

text = text.lower()
text = text.translate(str.maketrans("", "", string.punctuation))

tokens = word_tokenize(text)

stop_words = set(stopwords.words("english"))
filtered_tokens = [word for word in tokens if word not in stop_words]

word_freq = {}
for word in filtered_tokens:
    word_freq[word] = word_freq.get(word, 0) + 1

top_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]

print("Top words (cleaned):")
for word, freq in top_words:
    print(f"{word}: {freq}")
