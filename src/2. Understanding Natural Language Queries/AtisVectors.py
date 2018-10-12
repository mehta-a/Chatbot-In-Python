import spacy
import numpy as np

# Data set
sentences = []
with open('../../data/atis_queries.txt', 'rb') as f:
    for query in f.readlines():
        query = query.replace('\r\n', '')
        sentences.append(query)

print(sentences)

# Load the spacy model: nlp
nlp = spacy.load('en_core_web_md')

# Calculate the length of sentences
n_sentences = len(sentences)

# Calculate the dimensionality of nlp
embedding_dim = nlp.vocab.vectors_length

# Initialize the array with zeros: X
X = np.zeros((n_sentences, embedding_dim))

# Iterate over the sentences
for idx, sentence in enumerate(sentences):
    # Pass each each sentence to the nlp object to create a document
    doc = nlp(unicode(sentence))
    # Save the document's .vector attribute to the corresponding row in X
    X[idx, :] = doc.vector