# KEYWORD EXTRACTION                               
from keybert import KeyBERT
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np

def extract_keywords_with_keybert(article_text, top_n=10, diversity=0.5):
    model = KeyBERT(model="distilbert-base-nli-mean-tokens")

    keywords_with_scores = model.extract_keywords(
        article_text,
        top_n=top_n,
        keyphrase_ngram_range=(1, 2),
        stop_words="english",
        diversity=diversity
    )

    # Filter out similar keywords
    filtered_keywords = []
    vectorizer = CountVectorizer().fit([k[0] for k in keywords_with_scores])
    keyword_vectors = vectorizer.transform([k[0] for k in keywords_with_scores])

    for i, keyword in enumerate(keywords_with_scores):
        if i == 0:
            filtered_keywords.append(keyword)
            continue
        sim_scores = cosine_similarity(keyword_vectors[i], keyword_vectors[:i])
        if np.max(sim_scores) < 0.8:  # Threshold for similarity
            filtered_keywords.append(keyword)

    return filtered_keywords

data = [('greatest batsmen', 0.6964), ('icc champions', 0.546), ('scoring centuries', 0.4551), ('odi batsmen', 0.4279), ('cricketer decade', 0.4275), ('indian cricketer', 0.4174), ('international cricketer', 0.4038), ('male cricketer', 0.4019), ('batsmen history', 0.3895), ('international cricket', 0.3802)]

# Extract only the texts from the tuples
texts_only = [item[0] for item in data]

# Print the result
print(texts_only)

