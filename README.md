# SEC-Card-Game
A version of the HeatHack card game for the Scottish Episcopal Church; written in Jekyll with the Just the Docs template and relying on Liquid to render
many of the pages.

Done in a hurry to generate most of the website from CSV files so it's a mess :TODO: rationalise to be easy to update.

# Collections

Collections are generated from a spreadsheet using the scripts in aux.  To generate, open the Excel, copy all the cells on each tab and paste values in place, then save in a new
temporary filename.  Stick in aux/master-spreadsheet.xlsx.  Ensure there is a python environment with openpyxl and pandas installed.  I was installing tidyverse but most of it isn't  
needed.

python -m venv card-game-venv   --- to create virtual environment 
source card-game-venv/bin/activate --- to start using the virtual environment
python -m pip install openpyxl pandas

 and then:

cd aux
python generate-website.py

rm -rf ../collections/*
mv output/* ../collections

To test, 

cd ..
bundle exec jekyll serve -w --baseurl '' --port 4000


# Static pages

All markdown apart from the collections is hand-written, including a wildcard page (because otherwise this is hidden as it's not part of the petal/step/task navigation structure).


# Intended improvements

- change the representation of heat_air in the master spreadsheet, get cards 44 and 45 marked properly for heat_people.
- do the Excel fix to replace formulae with values automatically in the python, it's too painful this way.
- ideally, make the site build automatic
- discuss how to make it not a techy job to update the toolkit - spreadsheet is OK, but how do they change the markdown and static page structure? For individual pages, use https://www.writage.com/?
- check for/remove extraneous header material in markdown files
- make the css more rational

- fix the magic wand size and colouring, couldn't use what was provided, always rendered tiny

- discuss 
    - colours for petals and how to represent - coloured grid outline?  coloured icon?
    - colours for icons, placement for tag and wand icons
    - step and task icons, and fact we aren't using on website, breadcrumbs are sufficient and we don't want to look like a Pokemon card


# Tech notes

- the root directory appears to be different on the local build than on github.io, so the graphics don't appear during development.  To fix this, use e.g. href='{{ "/graphics/card_icons/maintenancerecords.svg" | relative_url }}'.  When testing locally use 
bundle exec jekyll serve -w --baseurl '' --port 4000


