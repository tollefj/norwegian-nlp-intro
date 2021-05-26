import sys
from argParser import ArgParser
from config.config import Config
from model import Model
from visualizer import Viz

def test(doc):
  print([(w.text, w.pos_) for w in doc])

  for token in doc:
      print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
              token.shape_, token.is_alpha, token.is_stop)

  print("----")
  for ent in doc.ents:
      print(ent.text, ent.start_char, ent.end_char, ent.label_)
  return doc


txt = "Capgemini har kontor på Sirkus Shopping, Falkenborgveien 9"

if __name__ == '__main__':
  args = ArgParser('SpaCy args')
  language = args.get_lang()

  conf = Config(language)
  if not conf.data:
    sys.exit(0)

  models = conf.get_models()
  views = ["parser", "ner", "textcat", "similarity", "tokens"]

  viz = Viz(conf.get_models(), views)
  viz.show(txt)
  
