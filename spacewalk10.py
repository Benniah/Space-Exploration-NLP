#!/usr/bin/python

""" 
DOCS , SPANS & ENTITIES FROM SCRATCH 

In this exercise, you’ll create the Doc and Span objects manually, 
and update the named entities – just like spaCy does behind the scenes. 
A shared nlp object has already been created.

 """

# Import the Doc and Span classes from spacy.tokens.
# Use the Doc class directly to create a doc from the words and spaces.
# Create a Span for “David Bowie” from the doc and assign it the label "PERSON".
# Overwrite the doc.ents with a list of one entity, the “David Bowie” span.

from spacy.lang.en import English

nlp = English()

# Import the Doc and Span classes
from spacy.tokens import Doc, Span

words = ["I", "like", "David", "Bowie"]
spaces = [True, True, True, False]

# Create a doc from the words and spaces
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc.text)

# Create a span for "David Bowie" from the doc and assign it the label "PERSON"
span = Span(doc, 2, 4, label="PERSON")
print(span.text, span.label_)

# Add the span to the doc's entities
doc.ents = [span]

# Print entities' text and labels
print([(ent.text, ent.label_) for ent in doc.ents])