import string
from collections import Counter
import matplotlib.pyplot as plt

emotions = []
stopwords_list = [
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves",
    "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was",
    "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and",
    "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between",
    "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off",
    "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
    "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too",
    "very", "s", "t", "can", "will", "just", "don", "should", "now"
]

# step 1 :-Read data from the file
with open("data.txt", encoding='utf8') as f:
    text = f.read()
    # setp 2 :-Lower case the file data
    lower_case = text.lower()
    # setp 3 :-Remove sepecial characters
    cleaned_text = lower_case.translate(
        str.maketrans('', '', string.punctuation))
    # step 4 :- Convert to token
    token = cleaned_text.split()
    # step 5 :- Remove stop words
    final_word = [word for word in token if word not in stopwords_list]
    # step 6 :- Extract emotions
    with open('emotions.txt', 'r') as e:
        for line in e:
            clear_line = line.replace("\n", '').replace(
                ",", '').replace("'", '').strip()
            word, emotion = clear_line.split(':')
            if word in final_word:
                emotions.append(emotion)
# step 6:- Convert to graph
e_count = Counter(emotions)
plt.bar(e_count.keys(), e_count.values())
plt.title("Sentiment-Analysis Graph")
plt.xlabel("Emotions")
plt.ylabel("Count")
plt.xticks(rotation=22)
plt.savefig("SA_graph.png")
plt.show()
