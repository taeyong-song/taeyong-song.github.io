---
layout: page
title: honors
permalink: /honors/
description: Honors, awards, and academic recognition.
nav: true
nav_order: 4
---

{% assign honors = site.data.profile.honors %}

{% if honors.size > 0 %}
<div class="editable-list">
{% for honor in honors %}
  <article class="editable-list__item editable-list__item--row">
    <div class="editable-list__year">{{ honor.year }}</div>
    <div>
      <h2>{{ honor.title }}</h2>
      <p class="editable-list__summary">{{ honor.organization }}</p>
      {% if honor.description %}<p>{{ honor.description }}</p>{% endif %}
    </div>
  </article>
{% endfor %}
</div>
{% else %}
<p class="empty-state">Honors and academic recognition will be updated here.</p>
{% endif %}
