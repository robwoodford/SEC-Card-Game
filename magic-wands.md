---
title: Magic Wands
layout: plain
nav_order: 4.4
parent: How to Use the Cards
--- 

<img src='{{ "/graphics/icons/magicwand.svg" | relative_url}}' alt=" " width="100px" height="100px"/>

If you feel stuck, it might help to look back at the magic wand cards.  These are the ones that can be real game-changers because they make a big change from "business as usual." 


<div>
  {% assign cards = site.cards | where: "magic_wand",1 %} 
  {% if cards == empty %}
  {% else %}
    <h2>Magic wand cards</h2>
    <div class="compact-grid-container">
      {% for card in cards %}
        <div class="wrap" onclick='location.href ="{{ card.url | relative_url }}";'>
               <div class="compact-icon">
                    <img class='card-icon' alt-text=' ' src='{{ "/graphics/icons/" | append: card.icon_shortcode | append: ".svg" | relative_url }}' >
                </div>
                <div class="compact-title">
                    {{ card.title }}
                </div>
        </div>
        {% endfor %}
    </div>
  {% endif %} 
</div>
