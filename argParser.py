
from argparse import ArgumentParser

def displacy_args():
  parser = ArgumentParser(description='SpaCy args')

  default_arg = object()

  parser.add_argument(
    '-s',
    '--serve',
    action='store',
    nargs='?',
    default=default_arg,
    help='Choose between serving the visualizations. True or false.'
  )

  args = parser.parse_args()
  return args.serve != default_arg