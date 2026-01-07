# Moby Dick Text Analysis with Python

A natural language processing project that analyzes the most frequent words in Herman Melville’s *Moby Dick* using Python.  
This project demonstrates a complete workflow from web data collection to text preprocessing and insight extraction.

---

## 📌 Project Overview

The goal of this project is to extract meaningful patterns from a large literary text using basic NLP techniques.  
By removing stopwords and analyzing word frequencies, we identify the main themes and narrative focus of the novel.

This project showcases practical skills in:
- Web data collection
- Text preprocessing
- Natural Language Processing (NLP)
- Data analysis with Python

---

## 🛠️ Technologies Used

- **Python**
- **Requests** – for downloading web data  
- **BeautifulSoup** – for HTML parsing  
- **NLTK** – for tokenization and stopword removal  
- **Collections.Counter** – for word frequency analysis  

---

## 📂 Project Structure


---

## 🔄 Workflow

1. **Data Collection**  
   - Downloaded the full text of *Moby Dick* from an online source using `requests`

2. **HTML Parsing**  
   - Extracted raw text using `BeautifulSoup`

3. **Text Preprocessing**  
   - Tokenized text using regular expressions  
   - Converted all words to lowercase  
   - Removed English stopwords using NLTK

4. **Analysis**  
   - Counted word frequencies using `Counter`  
   - Extracted the top 10 most common words

5. **Interpretation**  
   - Analyzed thematic patterns based on frequent keywords

---

## 📊 Key Findings

The most frequent words highlight the core themes of the novel:

- **"whale"**, **"sea"**, **"ship"** → Emphasize the maritime setting and central conflict  
- **"ahab"** → Reflects the dominance of Captain Ahab in the narrative  
- The vocabulary strongly supports the novel’s focus on obsession, fate, and human struggle

This shows how even simple NLP techniques can uncover meaningful patterns in large text documents.

---

jupyter notebook moby_dick_analysis.ipynb

💡 Why This Project Matters

This project demonstrates my ability to:

Work with real-world unstructured data

Apply text preprocessing techniques

Extract insights from large datasets

Communicate analytical results clearly

The same approach can be applied to:

News articles

Customer reviews

Social media data

Business reports

🚀 Future Improvements

Add data visualization (bar charts, word clouds)

Perform sentiment analysis

Apply topic modeling (LDA)

Compare multiple literary works

👤 Author

Minhyeok Choi

Aspiring Data Analyst / NLP Enthusiast
