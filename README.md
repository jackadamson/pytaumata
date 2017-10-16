# Pytaumata
For converting automata in to easy to use forms.


## Scripts:
graphs.py - for converting CSV files to JSON objects
```bash
python graphs.py states.csv > nfa.json
```
jsontodot.py - for converting the JSON in to a DOT format
```bash
python jsontodot.py nfa.json > nfa.dot
```
nfa.py - takes a csv and creates a pretty automata
```bash
python nfa.py states.csv
```
## Requirements
* [Python3](https://www.python.org/downloads/release/python-363/) because we're not barbarians
* [Graphviz](https://pypi.python.org/pypi/graphviz) which renders the graphs

![alt text](https://github.com/mrfluffybunny/pytaumata/blob/master/nfa.png?raw=true)
