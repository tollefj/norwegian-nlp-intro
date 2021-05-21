import spacy

class Model:
  def __init__(self, model):
    print("Initializing spacy with {}".format(model))
    self.nlp = spacy.load(model)
    self.doc = None

  def get(self):
    return self.nlp

  def parse(self, text):
    self.doc = self.nlp(text)

  def get_doc(self):
    return self.doc

  def get_entities(self):
    return self.doc.ents
