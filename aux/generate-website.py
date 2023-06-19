import pandas as pd
from string import Template
import os

# BUG - we get Nans for fields that require XLOOKUP unless I save
# a version of the spreadsheet with values only.

# park everything in a subdirectory so it's easy to delete/shift
temp_dir = "output"
master_datafile = "master-spreadsheet.xlsx"
collections = ["petals","tasks","steps","cards","tags"]

def build_collection (name):
    print("Building %s collection...\n" % name)
    try:
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
    except:
        print("Can't make main output directory!")
    coll_dir = ("_%s" % name)
    try:
        if not os.path.exists("%s/%s" % (temp_dir, coll_dir)):
            os.makedirs("%s/%s" % (temp_dir, coll_dir))
    except:
        print("Can't make directory for %s!" % name)
    df = pd.read_excel(master_datafile, sheet_name=name,dtype=str)
    df = df.fillna('')   
    if (name == "petals"):
        print(df)
    template = ("%s-template.txt" % name)
    try:
        with open(template, 'r') as f:
            src = Template(f.read())
    except:
        print("Can't read template for %s!" % name)
    for i in range(0,len(df)):
        result = src.substitute(df.iloc[i])
        try:
            outfilename = "%s/%s/%i.md" % (temp_dir, coll_dir, i)
            f = open(outfilename, "w")
            f.write(result)
            f.close()
        except:
            print("Can't write this file: %s" % outfilename)
    print("Finished with collection %s." % name)

for coll in collections:
    build_collection(coll)
