import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

emotions = []

# step 1 :-Read data from the file

with open("data.txt", encoding='utf8') as f:
    text = f.read()

    # setp 2 :-Lower case the file data
    lower_case = text.lower()

    # setp 3 :-Remove sepecial characters
    cleaned_text = lower_case.translate(
        str.maketrans('', '', string.punctuation))

    # step 4 :- Convert to token
    token = word_tokenize(cleaned_text, "english")

    # step 5 :- Remove stop words
    final_word = [
        word for word in token if word not in stopwords.words('english')]

    # step 6 :- Extract emotions
    with open('emotions.txt', 'r') as e:
        for line in e:
            clear_line = line.replace("\n", '').replace(
                ",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')
            if word in final_word:
                emotions.append(emotion)

# step 6:- Count the each emoticon
e_count = Counter(emotions)

# step 7:- Convert to graph
plt.bar(e_count.keys(), e_count.values())
plt.title("Sentiment-Analysis Graph")
plt.xlabel("Emotions")
plt.ylabel("Count")
plt.xticks(rotation=22)
plt.savefig("SA_graph.png")
plt.show()
