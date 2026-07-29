---
layout: page
permalink: /cv/
title: CV
nav: true
nav_order: 6
description: Academic background, research experience, publications, and activities.
---
{% assign profile = site.data.profile %}
{% if profile.identity.cv_pdf %}<p><a class="btn btn-sm btn-outline-primary" href="{{ profile.identity.cv_pdf | relative_url }}">Download CV (PDF)</a></p>{% endif %}
### Education
<div class="editable-list editable-list--compact">
{% for item in profile.education %}<article class="editable-list__item editable-list__item--row"><div class="editable-list__year">{{ item.period }}</div><div><h2>{{ item.degree }}</h2><p class="editable-list__summary">{{ item.institution }}</p><p>{{ item.description }}</p></div></article>{% endfor %}
</div>
### Research interests
{% for interest in profile.research_interests %}- {{ interest }}
{% endfor %}
### Honors
{% if profile.honors.size > 0 %}{% for honor in profile.honors %}- **{{ honor.title }}**, {{ honor.organization }} ({{ honor.year }})
{% endfor %}{% else %}To be updated.{% endif %}
