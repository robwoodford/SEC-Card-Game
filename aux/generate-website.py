import pandas as pd
from string import Template
import os

# :TODO: this crashes when it gets to the wildcard, but we don't really care as long as it's last.
# will matter if we automate.

df = pd.read_csv('petals.csv')

# park everything in a subdirectory so it's easy to delete/shift
tempdirname = "output"

if not os.path.exists(tempdirname):
    os.makedirs(tempdirname)

# make the petal markdown
with open('petals-template.txt', 'r') as f:
    src = Template(f.read())
    for i in range(0,len(df)):
        result = src.substitute(df.iloc[i])
        try:
            outfilename = "%s/p%i.md" % (tempdirname, df['number'].loc[i])
            f = open(outfilename, "w")
            f.write(result)
            f.close()
        except:
            print("Directory for this file doesn't exist: %s" % outfilename)

# make subdirs for the petal tasks 
for petal in df['number'].unique():
    dirname = "p%s" % petal
    fullpath = "%s/%s" % (tempdirname, dirname)
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)

#make the task markdown
# see if we can get away without a nav order, titles should do it as they're regular.
df = pd.read_csv('tasks.csv', dtype=str)

template = open('tasks-template.txt', 'r')
src = Template(template.read())
template.close()

for i in range(0,len(df)):
    result = src.substitute(df.iloc[i])
    # filenames are arbitrary, in file order from the csv.
    try: 
        outfilename = "./%s/p%s/%s.md" % (tempdirname, df['petal_number'].iloc[i], df['task_number'].iloc[i])
        f = open(outfilename, "w")
        f.write(result)
        f.close()
    except:
        print("Directory for this file doesn't exist: %s" % outfilename)

#print("Make subdirs for cards")
# make subdirs for the task cards
for i in range(0,len(df)):
    dirname = "%s" % df['task_number'].iloc[i]
    petalnum = "%s" % df['petal_number'].iloc[i]
    fullpath = "%s/p%s/%s" % (tempdirname, petalnum, dirname)
    if not os.path.exists(fullpath):
        os.makedirs(fullpath)

#make the card markdown
df = pd.read_csv('cards.csv', dtype=str)

template = open('cards-template.txt', 'r')
src = Template(template.read())
template.close()

print(df.columns)

for i in range(0,len(df)):
    result = src.substitute(df.iloc[i])
    # filenames are arbitrary, in file order from the csv.
    try: 
        outfilename = "./%s/p%s/%s/c%i.md" % (tempdirname, df['petal_number'].iloc[i], df['task'].iloc[i], i)
        #print("write card to: ",outfilename)
        f = open(outfilename, "w")
        f.write(result)
        f.close()
    except:
        print("Directory for this file doesn't exist: %s" % outfilename)