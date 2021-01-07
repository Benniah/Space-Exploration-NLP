#!/usr/bin/python

''' EXTRACTING COUNTRIES & RELATIONSHIPS
In the previous exercise, you wrote a script using spaCy’s 
PhraseMatcher to find country names in text. Let’s use that 
country matcher on a longer text, analyze the syntax and 
update the document’s entities with the matched countries.

'''
#Iterate over the matches and create a Span with the label "GPE" (geopolitical entity).
#Overwrite the entities in doc.ents and add the matched span.
#Get the matched span’s root head token.
#Print the text of the head token and the span.

import spacy
from spacy.matcher import PhraseMatcher
from spacy.tokens import Span
import json

with open("en/countries.json", encoding="utf8") as f:
    COUNTRIES = json.loads(f.read())
with open("en/country_text.txt", encoding="utf8") as f:
    TEXT = f.read()

nlp = spacy.load("en_core_web_sm")
matcher = PhraseMatcher(nlp.vocab)
patterns = list(nlp.pipe(COUNTRIES))
matcher.add("COUNTRY", None, *patterns)

# Create a doc and reset existing entities
doc = nlp(TEXT)
doc.ents = []

# Iterate over the matches
for match_id, start, end in matcher(doc):
    # Create a Span with the label for "GPE"
    span = Span(doc, start, end, label="GPE")

    # Overwrite the doc.ents and add the span
    doc.ents = list(doc.ents) + [span]

    # Get the span's root head token
    span_root_head = span.root.head
    # Print the text of the span root's head token and the span text
    print(span_root_head.text, "-->", span.text)

# Print the entities in the document
print([(ent.text, ent.label_) for ent in doc.ents if ent.label_ == "GPE"])

