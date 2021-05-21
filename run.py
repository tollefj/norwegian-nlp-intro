import sys
from argParser import displacy_args
from config import Config
from model import Model
import spacy_streamlit as lit

def test(doc):
  print([(w.text, w.pos_) for w in doc])

  for token in doc:
      print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

  print("----")
  for ent in doc.ents:
      print(ent.text, ent.start_char, ent.end_char, ent.label_)
  return doc


txt = "Dette er en presentasjon av norsk NLP for Capgemini som holdes på kontoret i Sirkus Shopping!"

if __name__ == '__main__':
  model_name = Config().get_model('nb')
  if not model_name:
    sys.exit(0)

  # model = Model(model_name)
  debug_models = [model_name, 'nb_core_news_sm']
  lit.visualize(debug_models, txt)
