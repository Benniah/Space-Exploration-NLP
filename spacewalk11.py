#!/usr/bin/python
""" DATA STRUCTURES BEST PRACTICES 
The code in this example is trying to analyze a text and collect
 all proper nouns that are followed by a verb.

"""

# Rewrite the code to use the native token attributes
# instead of lists of token_texts and pos_tags.
# Loop over each token in the doc and check the token.pos_ attribute.
# Use doc[token.i + 1] to check for the next token and its .pos_ attribute.
# If a proper noun before a verb is found, print its token.text.

import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("Berlin looks like a nice city")

# Iterate over the tokens
for token in doc:
    # Check if the current token is a proper noun
    if token.pos_ == "PROPN":
        # Check if the next token is a verb
        if doc[token.i + 1].pos_ == "VERB":
            print("Found proper noun before a verb:", token.text)