---
layout: page
permalink: /publications/
title: publications
description: Peer-reviewed work on building performance simulation and physics-embedded learning.
nav: true
nav_order: 2
---
{% assign publications = site.data.profile.publications | sort: "year" | reverse %}
<div class="editable-list">
{% for publication in publications %}
<article class="editable-list__item editable-list__item--row">
<div class="editable-list__year">{{ publication.year }}</div>
<div><h2>{% if publication.doi %}<a href="{{ publication.doi }}" target="_blank" rel="noopener">{{ publication.title }}</a>{% else %}{{ publication.title }}{% endif %}</h2><p>{{ publication.authors }}</p><p class="editable-list__summary">{{ publication.venue }}</p></div>
</article>
{% endfor %}
</div>
