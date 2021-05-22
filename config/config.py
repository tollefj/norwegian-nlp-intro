import yaml
import os

CONFIG_FILE = os.path.join(os.getcwd(), 'config', 'config.yaml')

class Config:
  def __init__(self, language):
    self.lang = language
    self.data = None
    with open(CONFIG_FILE, 'r') as conf:
      self.data = yaml.load(conf, Loader=yaml.FullLoader)

  def get_models(self):
    models = self.data.get('model').get(self.lang)
    return list(models.values())

  def get_model(self, large=True):
    _size = 'large' if large else 'small'
    return self.data.get('model').get(self.lang).get(_size)
    