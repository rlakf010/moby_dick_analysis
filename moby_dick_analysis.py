# Moby Dick Text Analysis with Python

This project performs basic text analysis on the novel *Moby Dick* by Herman Melville.
The goal is to extract the most frequent words from the text after cleaning and removing stopwords.

We use the following libraries:
- requests
- BeautifulSoup
- nltk
- collections.Counter

# Import necessary libraries
import requests
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from collections import Counter
import nltk

## Download NLTK Stopwords

We download the English stopwords list from NLTK.  
This step is required only once.

nltk.download('stopwords')

## Request the HTML Page

We send a request to the URL that contains the Moby Dick text
and store the response in a variable called `r`.

url = "https://s3.amazonaws.com/assets.datacamp.com/production/project_147/datasets/2701-h.htm"
r = requests.get(url)
r.encoding = 'utf-8'
html = r.text

## Create BeautifulSoup Object

We use BeautifulSoup to parse the HTML content.

html_soup = BeautifulSoup(html, "html.parser")

## Extract Text

We extract all the text content from the HTML file.

moby_text = html_soup.get_text()

## Tokenization

We use a regular expression tokenizer to split the text into words.
Only alphabetic characters are kept.

tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(moby_text)

## Convert to Lowercase

All words are converted to lowercase for consistency.

words = [word.lower() for word in tokens]

## Remove Stopwords

Stopwords are common words like "the", "and", "is" that do not add much meaning.
We remove them to focus on important words.

stop_words = stopwords.words('english')

words_no_stop = [
    word for word in words
    if word not in stop_words
]

## Count Word Frequencies

We use Counter to count how many times each word appears.

count = Counter(words_no_stop)

## Top 10 Most Common Words

We display the 10 most frequent words in the text.

top_ten = count.most_common(10)
print(top_ten)

## Results Interpretation

The most frequent words in *Moby Dick* reveal the main themes and focus of the novel.

Words such as **"whale"**, **"sea"**, **"ship"**, and **"captain"** appear repeatedly, indicating that the story strongly revolves around maritime life and the obsessive pursuit of the whale.

The frequent appearance of **"ahab"** highlights the central role of Captain Ahab and emphasizes his dominance in the narrative.  
This supports the idea that the novel is not only an adventure story but also a deep psychological exploration of obsession and revenge.

## Analytical Insight

By removing stopwords and analyzing word frequencies, we can focus on meaningful terms that carry thematic significance.  
This approach helps identify key motifs without manually reading the entire text.

For example, the dominance of words related to the sea and the whale reflects the novel’s intense focus on nature, fate, and human struggle.  
Such text analysis techniques are useful in literary studies, content analysis, and large-scale document processing.

## Conclusion

This project demonstrates how Python can be used to:
- Collect data from the web
- Clean and preprocess raw text
- Perform basic natural language processing
- Extract meaningful insights from large documents

The same workflow can be applied to news articles, customer reviews, social media data, and other real-world text datasets.  
This makes it a strong foundation for further work in data analysis, NLP, and machine learning.

## One-Line Summary

This analysis shows how simple NLP techniques can uncover thematic patterns in classic literature using Python.