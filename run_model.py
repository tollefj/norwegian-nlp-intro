import spacy
import operator

nlp = spacy.load("output/model-best")
text = ""
print("skriv Q for å avslutte")
# predict the sentiment until someone writes quit
if text != "Q":
    text = input("Issue tekst: ")
    doc = nlp(text)
    _sorted = [(x, round(y*100, 2)) for x, y in list(sorted(doc.cats.items(), key=operator.itemgetter(1),reverse=True))]
    print(_sorted)
    print('==> {}\n'.format(_sorted[0][0]))