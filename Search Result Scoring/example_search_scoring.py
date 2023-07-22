from bs4 import BeautifulSoup
import requests as req
import math
from collections import defaultdict

def preprocess_text(text):
    # We may want to implement text preprocessing here, like removing punctuation, converting to lowercase, etc.
    return text

def calculate_tf(word_freq, total_words):
    return word_freq / total_words

def calculate_idf(word, documents):
    num_documents_containing_word = sum(1 for document in documents if word in document)
    return math.log(len(documents) / (1 + num_documents_containing_word))

def calculate_tf_idf(document, query, documents):
    document = preprocess_text(document)
    query = preprocess_text(query)
    
    document_words = document.split()
    query_words = query.split()
    
    scores = defaultdict(float)
    for word in set(document_words + query_words):
        tf = calculate_tf(document_words.count(word), len(document_words))
        idf = calculate_idf(word, documents)
        scores[word] = tf * idf
    
    return sum(scores[word] for word in query_words)

def rank_search_results(query, documents):
    scores = [(document, calculate_tf_idf(document, query, documents)) for document in documents]
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores

# Scrape the bioparts repository and preprocess the text
page = req.get('http://parts.igem.org/Part:BBa_K3237027')
soup = BeautifulSoup(page.text, 'html.parser')
document_text = soup.get_text()

# We can scrape multiple pages and store their text in a list of documents
documents = [document_text]

query = "iGEM bioparts documentation"

search_results = rank_search_results(query, documents)

print("Search results scoring (TF-IDF):")
for rank, (document, score) in enumerate(search_results, start=1):
    print(f"{rank}. Score: {score:.4f}, Document: {document[:50]}...")
