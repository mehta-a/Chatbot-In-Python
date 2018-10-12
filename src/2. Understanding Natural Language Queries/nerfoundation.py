import spacy

nlp = spacy.load('en_core_web_md')

doc = nlp(u"my friends June works for Microsoft since 2012")

for ent in doc.ents:
    print(ent.text, ent.label_)

doc2 = nlp(u'a flight to bangalore from hyderabad')

bangalore, hyderabad = doc2[3], doc2[5]
print(list(bangalore.ancestors)[0])
print(list(hyderabad.ancestors)[0])

# assign roles
# Create the document
doc3 = nlp(u"let's see that jacket in red and some blue jeans")


def entity_type(token):
    token_str = str(token)
    item = [doc3[4], doc3[10]]
    color = [doc3[6], doc3[9]]
    if token_str in item:
        return "item"
    elif token_str in color:
        return "color"
    return "none"

# Iterate over parents in parse tree until an item entity is found
def find_parent_item(word):
    # Iterate over the word's ancestors
    for parent in word.ancestors:
        # Check for an "item" entity
        if entity_type(parent) == "item":
            return parent.text
    return None

# For all color entities, find their parent item
def assign_colors(doc):
    # Iterate over the document
    for word in doc:
        # Check for "color" entities
        if entity_type(word) == "color":
            # Find the parent
            item =  find_parent_item(word)
            print("item: {0} has color : {1}".format(item, word))

# Assign the colors
assign_colors(doc3)
