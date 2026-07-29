---
layout: archive
title: "CV"
permalink: /cv/
author_profile: true
redirect_from:
  - /resume
---

{% assign profile = site.data.profile %}

Education
======

{% for item in profile.education %}
- **{{ item.period }} — {{ item.degree }}**, {{ item.institution }}  
  {{ item.description }}
{% endfor %}

Research interests
======

{% for interest in profile.research_interests %}
- {{ interest }}
{% endfor %}

Publications
======

{% assign publications = profile.publications | sort: "year" | reverse %}
{% for publication in publications %}
- **{{ publication.year }} — {% if publication.doi %}[{{ publication.title }}]({{ publication.doi }}){% else %}{{ publication.title }}{% endif %}**  
  {{ publication.authors | replace: "Tae Yong Song", "<strong>Tae Yong Song</strong>" }}  
  *{{ publication.venue }}*
{% endfor %}

Activities
======

{% for group in profile.activities %}
### {{ group.category }}
{% for item in group.items %}
{% if group.category == "Research Presentations" %}
- {{ item.authors_html }} ({{ item.year }}). **{{ item.title }}**. *{{ item.venue }}*, {{ item.details }}.{% if item.award %} **{{ item.award }}**{% endif %}
{% else %}
- **{{ item.year }} — {{ item.title }}:** {{ item.description }}
{% endif %}
{% endfor %}
{% endfor %}

Honors
======

{% for honor in profile.honors %}
- **{{ honor.year }} — {% if honor.certificate_url %}[{{ honor.title }}]({{ honor.certificate_url }}){% else %}{{ honor.title }}{% endif %}**{% if honor.organization %}, {{ honor.organization }}{% endif %}
{% endfor %}
