import pandas as pd
from string import Template

df = pd.read_csv('cards.csv', dtype=str)

with open('cards-template.txt', 'r') as f:
    src = Template(f.read())
    for i in range(0,len(df)):
        result = src.substitute(df.iloc[i])
        # filenames are arbitrary, in file order from the csv.
        outfilename = "c%i.md" % i
        f = open(outfilename, "w")
        f.write(result)
        f.close()