import json
import sys

graph = {}
with open(sys.argv[1]) as graphfile:
    graph = json.load(graphfile)
print("digraph automata {")
for s in graph["finalstates"]:
    print("    " + s + " [shape=doublecircle];")
    
for s in graph["states"]:
    if s not in graph["finalstates"]:
        print("    " + s + " [shape=circle];")
    
for t in graph["transitions"]:
    for dst in t["dsts"]:
        print("    " + t["src"] + " -> " + dst + '[label="' + t["token"] + '"];')
print("}")