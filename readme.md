# Sentiment Analyser ML Project

- [YouTube Video](https://www.youtube.com/watch?v=dyN_WtjdfpA)
- [GeeksforGeeks - NLP Tokenization](https://www.geeksforgeeks.org/nlp-how-tokenizing-text-sentence-words-works/)
- [GeeksforGeeks - Pyplot in Matplotlib](https://www.geeksforgeeks.org/pyplot-in-matplotlib/)

## Tokenization

Tokenization in the realm of Natural Language Processing (NLP) and machine learning refers to the process of converting a sequence of text into smaller parts, known as tokens. These tokens can be as small as characters or as long as words.

## Stop Words

Stop words are a set of commonly used words in a language. Examples of stop words in English are “a,” “the,” “is,” “are,” etc. Stop words are commonly used in Text Mining and Natural Language Processing (NLP) to eliminate words that are so widely used that they carry very little useful information.

```python
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

stopwords_list = [...]  # List of stop words

# Step 1: Read text from file
with open("read.txt", encoding="utf-8") as file:
    text = file.read()

# Step 2: Convert to lowercase
lower_case = text.lower()

# Step 3: Remove special characters
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Step 4: Convert into tokens
tokenized_words = cleaned_text.split()

# Step 5: Remove stopwords
final_words = [word for word in tokenized_words if word not in stopwords]

# Step 6: Extract emotions from the emotion file
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

# Step 7: Count the number of each emotion
e_count = Counter(emotions)

# Step 8: Convert to graph
plt.bar(e_count.keys(), e_count.values())
plt.title("Sentiment-Analysis Graph")
plt.xlabel("Emotions")
plt.ylabel("Count")
plt.xticks(rotation=22)
plt.savefig("SA_graph.png")
plt.show()

# Using NLTK (Natural Language Toolkit)

# Step 4: Convert into tokens
token = word_tokenize(cleaned_text, "english")

# Step 5: Remove stopwords
final_word = [word for word in token if word not in stopwords.words('english')]
```

Customization
Color Customization

You can customize the color of the bars using the color parameter. For example:

```python
plt.bar(x_values, y_values, color='skyblue')
```

Bar Width

Adjust the width of the bars using the width parameter:

```python

plt.bar(x_values, y_values, width=0.5)
```

Labels and Title

Add labels to the x-axis, y-axis, and a title to the plot for better clarity:

```python

plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Bar Chart Title')
```

Legend

If you have multiple sets of data, you can add a legend:

```python

plt.bar(x1, y1, label='Data 1')
plt.bar(x2, y2, label='Data 2')
plt.legend()
```

Grid

Add a grid to make it easier to read values from the plot:

```python

plt.grid(True, axis='y', linestyle='--', alpha=0.7)
```

Annotations

Annotate specific bars with additional information:

```python

plt.annotate('Max Value', xy=(max_x, max_y), xytext=(max_x, max_y + 5), arrowprops=dict(facecolor='red', shrink=0.05))
```

Horizontal Bar Chart

If you prefer horizontal bars:

```python

plt.barh(y_values, x_values)
```

Stacked Bar Charts

Create stacked bar charts for visualizing the contribution of each category:

```python

plt.bar(x_values, y1, label='Category 1')
plt.bar(x_values, y2, bottom=y1, label='Category 2')
plt.legend()
```

Error Bars

If you have error information, you can add error bars:

```python

plt.bar(x_values, y_values, yerr=error_values, capsize=5)
```

Bar Labels

Display the values on top of each bar:

```python

for i, value in enumerate(y_values):
    plt.text(i, value + 0.1, str(value), ha='center')
```
