---
layout: page
title: about
permalink: /
nav: true
nav_order: 1
---
{% assign profile = site.data.profile %}
<section class="profile-hero">
  <div class="profile-hero__media">
    <img src="{{ profile.identity.photo | relative_url }}" alt="Portrait of {{ profile.identity.name }}">
    <div class="profile-hero__links">{% for link in profile.links %}<a href="{{ link.url | relative_url }}"{% if link.url contains 'http' %} target="_blank" rel="noopener"{% endif %}>{{ link.label }}</a>{% endfor %}</div>
  </div>
  <div class="profile-hero__content">
    <p class="profile-hero__eyebrow">{{ profile.identity.role }} · {{ profile.identity.field }}</p>
    <h1>{{ profile.identity.name }}</h1>
    <p class="profile-hero__affiliation">{{ profile.identity.department }}<br>{{ profile.identity.affiliation }}</p>
    {% for paragraph in profile.about %}<p>{{ paragraph }}</p>{% endfor %}
  </div>
</section>
### Research interests
{% for interest in profile.research_interests %}- {{ interest }}
{% endfor %}
### Selected publications
{% assign selected_publications = profile.publications | where: "selected", true %}
{% for publication in selected_publications limit: 3 %}<div class="publication-row"><span>{{ publication.year }}</span><div><strong>{{ publication.title }}</strong><p>{{ publication.venue }}</p></div></div>{% endfor %}
