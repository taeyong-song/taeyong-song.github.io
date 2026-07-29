---
layout: page
title: activities
permalink: /activities/
description: Research presentations, service, and academic activities.
nav: false
nav_order: 5
---

{% assign activity_groups = site.data.profile.activities %}

{% for group in activity_groups %}
### {{ group.category }}

<div class="editable-list editable-list--compact">
{% for item in group.items %}
  <article class="editable-list__item editable-list__item--row">
    <div class="editable-list__year">{{ item.year }}</div>
    <div>
      <h2>{{ item.title }}</h2>
      <p>{{ item.description }}</p>
    </div>
  </article>
{% endfor %}
</div>
{% endfor %}
