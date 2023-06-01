import pandas as pd
from string import Template
import os

df = pd.read_csv('tasks.csv', dtype=str)

# see if we can get away without a nav order, titles should do it as they're regular.

for petal in df['petal_number'].unique():
    dirname = "p%s" % petal
    if not os.path.exists(dirname):
        os.makedirs(dirname)

with open('tasks-template.txt', 'r') as f:
    src = Template(f.read())
    for i in range(0,len(df)):
        result = src.substitute(df.iloc[i])
        # filenames are arbitrary, in file order from the csv.
        outfilename = "./p%s/%s.md" % (df['petal_number'].iloc[i], df['title'].iloc[i])
        f = open(outfilename, "w")
        f.write(result)
        f.close()