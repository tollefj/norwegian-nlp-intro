import yaml

class Config:
  def __init__(self):
    with open(r'config.yaml') as conf:
      self.data = yaml.load(conf, Loader=yaml.FullLoader)

  def get_model(self, lang='nb'):
    return self.data.get('model').get(lang)