
import pandas as pd
from string import Template

petals_df = pd.read_csv('petals.csv')

with open('petals-template.txt', 'r') as f:
    src = Template(f.read())
    for i in range(0,len(petals_df)):
        result = src.substitute(petals_df.iloc[i])
        outfilename = "p%i.md" % (petals_df['number'].loc[i])
        f = open(outfilename, "w")
        f.write(result)
        f.close()






    