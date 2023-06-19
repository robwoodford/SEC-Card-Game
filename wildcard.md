---
layout: default
title: Wildcard
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

<!-- :TODO: fix formatting -->
<!--
<img class='card-icon' alt-text=' ' src='/graphics/icons/wildcard.svg'>
<h1>Wildcard</h1>

<p>We can’t think of everything that might suit your circumstances.  For instance, one church could get their hall warm after they built a buggy park outside - because otherwise when the children came in, all the heat escaped.  You'll need to be curious about your building and your users to use this card well.</p> 

-->