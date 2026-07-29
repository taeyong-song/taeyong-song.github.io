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
  {{ publication.authors }}  
  *{{ publication.venue }}*
{% endfor %}

Activities
======

{% for group in profile.activities %}
### {{ group.category }}
{% for item in group.items %}
- **{{ item.year }} — {{ item.title }}:** {{ item.description }}
{% endfor %}
{% endfor %}

Honors
======

{% for honor in profile.honors %}
- **{{ honor.year }} — {% if honor.certificate_url %}[{{ honor.title }}]({{ honor.certificate_url }}){% else %}{{ honor.title }}{% endif %}**{% if honor.organization %}, {{ honor.organization }}{% endif %}
{% endfor %}
