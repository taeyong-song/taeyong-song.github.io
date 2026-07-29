---
layout: archive
title: "Research Projects"
permalink: /research-projects/
author_profile: true
---

{% assign profile = site.data.profile %}
{% assign sorted_projects = profile.projects | sort: "sort_date" | reverse %}

My research projects connect building simulation, digital twins, causal evaluation, and data-driven intelligence with practical design and operational problems.

<div class="research-project-list">
{% for project in sorted_projects %}
  <article class="research-project-record">
    <div class="research-project-record__index">0{{ forloop.index }}</div>
    <div class="research-project-record__body">
      <div class="research-project-record__meta">
        <span class="research-project-record__year">{{ project.sort_date | slice: 0, 4 }}</span>
        <span>{{ project.period }}</span>
        <span>{{ project.sponsor }}</span>
      </div>
      <h2 class="research-project-record__title">{{ project.title }}</h2>
      <p class="research-project-record__description">{{ project.description }}</p>
      {% if project.image %}
      <img class="research-project-record__image" src="{{ project.image }}" alt="{{ project.title }}">
      {% endif %}
    </div>
  </article>
{% endfor %}
</div>
