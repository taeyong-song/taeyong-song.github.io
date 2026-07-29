---
permalink: /
title: "Tae Yong Song"
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

{% for interest in profile.research_interests %}
- {{ interest }}
{% endfor %}

## Selected publications

{% assign selected_publications = profile.publications | where: "selected", true %}
{% for publication in selected_publications %}
**{% if publication.doi %}[{{ publication.title }}]({{ publication.doi }}){% else %}{{ publication.title }}{% endif %}**  
{{ publication.authors | replace: "Tae Yong Song", "<strong>Tae Yong Song</strong>" }}  
*{{ publication.venue }}*, {{ publication.year }}

{% endfor %}

[View all publications](/publications/)

## Research projects

My project portfolio includes building-energy digital twins, automated BEM workflows, causal net-zero design evaluation, green-remodeling diagnostics, and HVAC prediction and control.

[View all research projects →](/research-projects/)

## Education

{% for item in profile.education %}
**{{ item.degree }}**, {{ item.institution }}  
{{ item.period }} · {{ item.description }}

{% endfor %}

## Activities & honors

{% for group in profile.activities %}
### {{ group.category }}
{% for item in group.items %}
{% if group.category == "Research Presentations" %}
- {{ item.authors_html }} ({{ item.year }}). **{{ item.title }}**. *{{ item.venue }}*, {{ item.details }}.{% if item.award %} <strong style="color:#b26a00;">{{ item.award }}</strong>{% endif %}
{% else %}
- **{{ item.year }} — {{ item.title }}:** {{ item.description }}
{% endif %}
{% endfor %}
{% endfor %}

{% for honor in profile.honors %}
- **{{ honor.year }} — {% if honor.certificate_url %}[{{ honor.title }}]({{ honor.certificate_url }}){% else %}{{ honor.title }}{% endif %}**{% if honor.organization %}, {{ honor.organization }}{% endif %}
{% endfor %}
