---
title: Magic Wands
layout: plain
nav_order: 2.4
parent: How to Use the Cards
--- 

<img src="graphics/icons/magicwand.svg" alt=" " width="100px" height="100px"/>

If you feel stuck, it might help to look back at the magic wand cards.  These are the ones that can be real game-changers because they make a big change from "business as usual." 

<div>
      Magic wand cards:
      {% assign cards = site.cards | where: "magic_wand",1 %} 
      <ul>
      
          {% for card in cards %}
          <li><a href="{{ card.url }}">{{ card.title }} </a></li>
          {% endfor %}
      </ul>
</div>