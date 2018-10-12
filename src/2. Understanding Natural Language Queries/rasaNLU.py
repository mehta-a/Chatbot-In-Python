'''
RASA
- Library for intent recognition & entity extraction
- Based on spaCy, scikit-learn, & other libraries
- Built in support for chatbot specific tasks

Robust language understanding with rasa NLU

'''

from rasa_nlu.converters import load_data
from rasa_nlu.config import RasaNLUConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter

training_data = load_data('../../data/training_data.json')
config = RasaNLUConfig(cmdline_args={"pipeline": "spacy_sklearn"})
trainer = Trainer(config)

interpreter = trainer.train(training_data)

#
#
# import json
#
# print(json.dumps(data.training_examples[22], indent=2))

message = u"I want to book a flight to London."

print(interpreter.parse(message))

spacy_sklearn_pipeline = [
  "nlp_spacy",  # spacy english component
  "ner_crf",    # CRF for entity recognition
  "ner_synonyms",   # Finding similar entities
  "intent_featurizer_spacy",    # building vectors using spacy
  "intent_classifier_sklearn",   # svm based intent classifier
    "intent_featurizer_ngrams"  # handling typos
]
RasaNLUConfig(
            cmdline_args={"pipeline": spacy_sklearn_pipeline}
        )