---
permalink: /
title: "About Me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

{% assign profile = site.data.profile %}

## Welcome to Tae Yong's page

{% for paragraph in profile.about %}
{{ paragraph }}

{% endfor %}

My work connects **physical knowledge** with **data-driven learning** so that building models remain interpretable, transferable, and useful for decisions when operational data are limited.

### Research interests

<ul class="research-keywords" aria-label="Research interests">
{% for interest in profile.research_interests %}
  <li class="research-keyword">{{ interest }}</li>
{% endfor %}
</ul>

## Selected publications

    {% assign selected_publications = profile.publications | where: "category", "international_journal" %}
{% for publication in selected_publications %}
**{% if publication.doi %}[{{ publication.title }}]({{ publication.doi }}){% else %}{{ publication.title }}{% endif %}**  
{{ publication.authors | replace: "Tae Yong Song", "<strong>Tae Yong Song</strong>" }}  
*{{ publication.venue }}*, {{ publication.year }}

{% endfor %}

[View all publications](/publications/)

## Research projects

My project portfolio includes building-energy digital twins, automated BEM workflows, causal net-zero design evaluation, green-remodeling diagnostics, and HVAC prediction and control.

[View all research projects](/research-projects/)

## Education

{% for item in profile.education %}
**{{ item.degree }}**, {{ item.institution }}{% if item.advisor %} (Advisor: {{ item.advisor }}){% endif %}<br>
{{ item.period }}{% if item.thesis %}<br>{% endif %}
{% if item.thesis %}Thesis: {{ item.thesis }}{% endif %}

{% endfor %}

## Teaching

{% for group in profile.activities %}
{% for item in group.items %}
- **{{ item.year }} — {{ item.title }}:** {{ item.description }}
{% endfor %}
{% endfor %}
