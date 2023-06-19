---
title: Quick Wins
layout: plain
nav_order: 2.3
parent: How to Use the Cards
--- 

<img class="toolkit-icon" alt="{{ tag.alt_text }}" src=' {{ "/graphics/icons/quick.svg" | relative_url }}'>

There are a number of actions that we consider to be quick wins - things that might be relatively easy to do and immediately reduce your energy bill.  

<img src='{{"graphics/IsometricChurch-QuickWins2-01-01.jpg" | relative_url }}' alt=" " title="annotated card front" width="750px"/>

{: .note }
The selection of quick wins is still under review.


<div>
      Quick win cards:
      {% assign cards = site.cards | where: "easy_wins",1 %} 
      <ul>
      
          {% for card in cards %}
          <li><a href="{{ card.url | relative_url }}">{{ card.title }} </a></li>
          {% endfor %}
      </ul>
      </div>