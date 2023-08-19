---
layout: default
title: Wildcard
nav_order: 4.2
parent: How to use the Cards
quote: To invent, you need a good imagination and a pile of junk.
quote-attribution: Thomas A. Edison
category: nan
card_icon: wildcard.svg
space: nan
carbon_stars: nan
cost: nan
easy_wins: nan
magic_wand: nan
step_number: nan
cardpetal_tag: magicwand.svg
cardpetal_colour: othercolour.svg
card_icon_html: <img class='card-icon' alt-text=' ' src='/graphics/icons/wildcard.svg'>
nav_order: 100
---
There is one wildcard in the card pack.  It doesn't fit into any of the petals.

{% assign wild = site.cards | where: "title", "Wildcard" | first %} 


<div class="wrap" onclick='location.href ="{{ wild.url | relative_url }}";'>
                <div class="list-row">
                    
                   <div class="list-icon">
                        <img class='toolkit-icon' alt-text=' ' src='{{ "/graphics/icons/" | append: wild.icon_shortcode | append: ".svg" | relative_url }}' >
                    </div>
                    <div class="list-description">
                         {{  wild.title | append: "<br/>"  }} 
                    </div>   
                
                </div>
            </div>

