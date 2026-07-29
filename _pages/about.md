---
layout: about
title: about
permalink: /
subtitle: Ph.D. student · Building Science · Seoul National University

profile:
  align: left
  image: prof_pic.jpg
  image_circular: false
  more_info: >
    <p><strong>Tae Yong Song</strong></p>
    <p>Department of Architecture and Architectural Engineering<br>Seoul National University</p>

selected_papers: true
social: false
announcements:
  enabled: false
latest_posts:
  enabled: false
---

{% assign profile = site.data.profile %}

<p class="profile-links">
{% for link in profile.links %}
  <a href="{{ link.url | relative_url }}"{% if link.url contains 'http' %} target="_blank" rel="noopener"{% endif %}>{{ link.label }}</a>{% unless forloop.last %} · {% endunless %}
{% endfor %}
</p>

{% for paragraph in profile.about %}
{{ paragraph }}

{% endfor %}

### Research interests

{% for interest in profile.research_interests %}
- {{ interest }}
{% endfor %}
