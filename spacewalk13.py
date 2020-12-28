#!/usr/bin/python

""" COMPARING SIMILARITIES 
In this exercise, you’ll be using spaCy’s similarity methods to compare Doc,
 Token and Span objects and get similarity scores.
"""

print('***********************************')
print('PART 1 - Docs')
print('***********************************')
# Use the doc.similarity method to compare doc1 to doc2 and print the result.

import spacy

nlp = spacy.load("en_core_web_md")

doc1 = nlp("It's a warm summer day")
doc2 = nlp("It's sunny outside")

# Get the similarity of doc1 and doc2
similarity = doc1.similarity(doc2)
print(similarity)

print('***********************************')
print('PART 2 - Tokens')
print('***********************************')
# Use the token.similarity method to compare token1 to token2 and print the result.

import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("TV and books")
token1, token2 = doc[0], doc[2]

# Get the similarity of the tokens "TV" and "books"
similarity = token1.similarity(token2)
print(similarity)

print('***********************************')
print('PART 3 - Spans')
print('***********************************')
# Create spans for “great restaurant”/“really nice bar”.
# Use span.similarity to compare them and print the result.

import spacy

nlp = spacy.load("en_core_web_md")

doc = nlp("This was a great restaurant. Afterwards, we went to a really nice bar.")

# Create spans for "great restaurant" and "really nice bar"
span1 = doc[3:5]
span2 = doc[12:15]

# Get the similarity of the spans
similarity = span1.similarity(span2)
print(similarity)