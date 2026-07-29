---
layout: page
title: projects
permalink: /projects/
description: Research themes and ongoing work.
nav: false
nav_order: 3
---

{% assign projects = site.data.profile.projects %}

<div class="editable-list">
{% for project in projects %}
  <article class="editable-list__item">
    <p class="editable-list__index">0{{ forloop.index }}</p>
    <h2>{{ project.title }}</h2>
    <p class="editable-list__summary">{{ project.summary }}</p>
    <p>{{ project.description }}</p>
    {% if project.related_url %}
      <a href="{{ project.related_url | relative_url }}">Related publications →</a>
    {% endif %}
  </article>
{% endfor %}
</div>
