#!/usr/bin/python

'''Predicting Part-of_speech Tags'''
import spacy

# Load the small English model 
nlp = spacy.load("en_core_web_sm")

# Process a text 
doc = nlp(" I love Machine learning and Neural Networks"
          " I watch a lot of Science fiction Movies "
          " I watch a lot of Action Movies "
          " Can we go for dinner tonight ? "
          " What are your plans this christmas ? "
          
          )

# Iterate over the tokens 
for token in doc:
    # print the text and the predicted part-of-speech tag
    print(token.text, token.pos_)

print('########################')

'''Predicting Syntactic Dependencies'''

for token in doc:
     print(token.text, token.pos_, token.dep_, token.head.text)