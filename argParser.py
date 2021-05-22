
from argparse import ArgumentParser

class ArgParser():
  def __init__(self, description = 'Arguments'):
    self.parser = ArgumentParser(description=description)
    self.default_arg = object()

    self.add_args()

  def add_args(self):
    self.parser.add_argument(
      '-s',
      '--serve',
      action='store',
      nargs='?',
      default=self.default_arg,
      help='Choose between serving the visualizations. True or false.'
    )

    self.parser.add_argument(
      '-l'
      '--lang',
      dest='lang',
      default='nb',
      help='English (en) or Norwegian (nb)'
    )

    self.args = self.parser.parse_args()

  def to_serve(self):
    return self.args.serve != default_arg

  def get_lang(self):
    return self.args.lang or None
