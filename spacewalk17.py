''' PROCESSING PIPELINES
Here, we shall begin to explore SpaCy's Processing Pipeline and
learn what goes on under the hood when you process a text, how to
write your own components and add them to the pipeline, and how to
use custom attributes to add your own metadata to the documents, spans and tokens.
'''
# Load the en_core_web_sm model and create the nlp object.
# Print the names of the pipeline components using nlp.pipe_names.
# Print the full pipeline of (name, component) tuples using nlp.pipeline.

import spacy

# Load the en_core_web_sm model
nlp = spacy.load("en_core_web_sm")

# Print the names of the pipeline components
print(nlp.pipe_names)

# Print the full pipeline of (name, component) tuples
print(nlp.pipeline)