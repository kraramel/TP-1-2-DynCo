import codecs
from pyld import jsonld
import json
from pyshacl import validate

# Commande pour télécharger la trace : python .\import_github_trace.py  'pchampin/sophia_rs' --out './trace.json'
# Lecture trace et context
with open('trace.json') as myfile:
    doc = json.load(myfile)

with open('context.json') as myfile:
    context = json.load(myfile)

expanded = jsonld.expand(doc, {'expandContext': context})

with open('expanded.json', 'w') as f:
    json.dump(expanded, f, indent=2)

nquads = jsonld.normalize(
    expanded, {'algorithm': 'URDNA2015', 'format': 'application/n-quads'})

with codecs.open('nquads.nq', 'w', 'utf-8') as f:
    f.write(nquads)