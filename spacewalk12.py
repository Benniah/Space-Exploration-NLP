#!/usr/bin/python

""" INSPECTING WORD VECTORS 
In this exercise, we use a larger English model, which includes 
around 20.000 word vectors. The model is already pre-installed.
"""
# Load the medium "en_core_web_md" model with word vectors.
# Print the vector for "bananas" using the token.vector attribute.

import spacy

# Load the en_core_web_md model
nlp = spacy.load("en_core_web_md")

# Process a text
doc = nlp("Two bananas in pyjamas")

# Get the vector for the token "bananas"
bananas_vector = doc[1].vector
print(bananas_vector)