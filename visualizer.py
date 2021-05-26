import spacy_streamlit as lit

class Viz:
  def __init__(self, models, views = None):
    self.views = views
    self.models = models

  def set_views(self, views):
    self.views = views

  def set_models(self, models):
    self.models = models

  def show(self, text, meta=False):
    lit.visualize(
      models=self.models,
      default_text=text,
      default_model=self.models[0],
      visualizers=self.views,
      similarity_texts=('datamaskin', 'laptop'),
      show_json_doc=meta,
      show_meta=meta,
      show_config=meta,
      show_visualizer_select=True,
      sidebar_title='NLP spaCy intro',
      show_logo=False,
      # color='#EEF5DB',
    )
