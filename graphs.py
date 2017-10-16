import csv
import sys
import json

with open(sys.argv[1]) as csvfile:
    csvreader = csv.reader(csvfile)
    rows = list(csvreader)
alphabet = rows[0][2:]
states = [row[0] for row in rows[1:]]
finalstates = []
transitions = []
for row in rows[1:]:
    if row[1] == "t":
        finalstates.append(row[0])
    for col in range(len(alphabet)):
        if len(row[col+2]) > 0:
            transitions.append({"src":row[0],"token":alphabet[col],"dsts":row[col+2].split("+")})

nfa = {"initial":states[0],"states":states,"alphabet":alphabet,"transitions":transitions, "finalstates":finalstates}
print(json.dumps(nfa, sort_keys=True,indent=4, separators=(',', ': ')))