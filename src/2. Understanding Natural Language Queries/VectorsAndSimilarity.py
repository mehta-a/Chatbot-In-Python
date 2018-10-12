import spacy

nlp = spacy.load('en_core_web_md')

doc = nlp(u'hello can you help me?')

for token in doc:
    print("{} : {}".format(token, token.vector[:3]))

# similarity : direction of vectors matters, the distance between words = angle between the vectors
# cosine similarity : 1 (vectors in same direction); 0: (vectors are perpendicular); -1 (if vectors point in opposite)

doc1 = nlp(u'cat you please help me?')

sim_score = doc1.similarity(doc)
print(sim_score)