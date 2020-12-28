#!/usr/bin/python

""" STRINGS TO HASHES """

print('***********************************')
print('PART 1')
print('***********************************')
# Look up the string “cat” in nlp.vocab.strings to get the hash.
# Look up the hash to get back the string.

from spacy.lang.en import English

nlp = English()
doc = nlp("I have a cat")

# Look up the hash for the word "cat"
cat_hash = nlp.vocab.strings["cat"]
print(cat_hash)

# Look up the cat_hash to get the string
cat_string = nlp.vocab.strings[cat_hash]
print(cat_string)

print('***********************************')
print('PART 2')
print('***********************************')
# Look up the string label “PERSON” in nlp.vocab.strings to get the hash.
# Look up the hash to get back the string.

import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("David Bowie is a PERSON")

# Look up the hash for the string label "PERSON"
person_hash = nlp.vocab.strings["PERSON"]
print(person_hash)

# Look up the person_hash to get the string
person_string = nlp.vocab.strings[person_hash]
print(person_string)