---
layout: archive
title: "Honors"
permalink: /honors/
author_profile: true
---

{% assign profile = site.data.profile %}

<div class="honors-list">
{% for honor in profile.honors %}
  <article class="honor-record">
    <div class="honor-record__year">{{ honor.year }}</div>
    <div>
      <h2 class="honor-record__title">{{ honor.title }}</h2>
      <p class="honor-record__proceedings">{{ honor.proceedings }}</p>
      {% if honor.certificate_url %}
      <a class="honor-record__pdf" href="{{ honor.certificate_url }}" target="_blank" rel="noopener">PDF</a>
      {% endif %}
    </div>
  </article>
{% endfor %}
</div>
