---
layout: archive
title: "Research Projects"
permalink: /research-projects/
author_profile: true
---

{% assign profile = site.data.profile %}

My research projects connect building simulation, digital twins, causal evaluation, and data-driven intelligence with practical design and operational problems.

{% for project in profile.projects %}
<article class="research-project-entry">
  {% if project.image %}
  <img src="{{ project.image }}" alt="{{ project.title }}">
  {% endif %}

  ## {{ project.title }}

  *Korean title: {{ project.korean_title }}*  
  **{{ project.period }} · {{ project.sponsor }}**

  **{{ project.summary }}**  
  {{ project.description }}
</article>
{% endfor %}
