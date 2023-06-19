---
title: Heating Strategy
layout: plain
nav_order: 2.5
parent: How to Use the Cards
--- 

One thing you'll want to do early on is decide on your heating strategy.  Will you use the building enough and can you address heat loss well enough that you will heat the air and keep it inside the building as well as you can, or will you instead choose to heat the people?  

It's not an all-or-nothing choice.  You might heat the people in some spaces and heat the air in others, or you can also heat the air a bit and the people a bit, depending on your circumstances.

Some cards are really important for heating the air and some are only about heating the people - you can find them by looking for these symbols.  If you decide to change to heating the people, but it will take a while to organise, don't forget to still consider doing some of the quick win cards for your current heating systems.

<div class="list-grid-container">
    <div class= "list-row">
        <div class="list-icon">
            <img class="toolkit-icon" alt=" Heat the Air " src="/graphics/icons/heatair.svg">
        </div>
        <div class="list-description">
            Heat the Air &mdash; also called "space heating"
        </div>
    </div>

   
    <div class= "list-row">
        <div class="list-icon">
            <img class="toolkit-icon" alt=" Heat the Air " src="/graphics/icons/heatpeople.svg">
        </div>
        <div class="list-description">
            Heat the People &mdash; also called "localised heating"
        </div>
    </div>
</div>


<div>
     Heat the air cards:
      {% assign cards = site.cards | where: "heat_air",1 %} 
      <ul>
      
          {% for card in cards %}
          <li><a href="{{ card.url }}">{{ card.title }} </a></li>
          {% endfor %}
      </ul>
</div>

<div>
     Heat the people cards:
      {% assign cards = site.cards | where: "heat_people",1 %} 
      <ul>
      
          {% for card in cards %}
          <li><a href="{{ card.url }}">{{ card.title }} </a></li>
          {% endfor %}
      </ul>
</div>