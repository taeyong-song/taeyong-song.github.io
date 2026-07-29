---
layout: page
title: home
permalink: /
nav: true
nav_order: 1
---
{% assign profile = site.data.profile %}
<section class="profile-hero">
{% if profile.identity.photo %}
<div class="profile-hero__media"><img src="{{ profile.identity.photo | relative_url }}" alt="Portrait of {{ profile.identity.name }}"><div class="profile-hero__links">{% for link in profile.links %}<a href="{{ link.url | relative_url }}"{% if link.url contains 'http' %} target="_blank" rel="noopener"{% endif %}>{{ link.label }}</a>{% endfor %}</div></div>
{% endif %}
<div class="profile-hero__content"><p class="profile-hero__eyebrow">{{ profile.identity.role }} · {{ profile.identity.field }}</p><h1>{{ profile.identity.name }}</h1><p class="profile-hero__affiliation">{{ profile.identity.department }}<br>{{ profile.identity.affiliation }}</p>{% for paragraph in profile.about %}<p>{{ paragraph }}</p>{% endfor %}<div class="profile-hero__links">{% for link in profile.links %}<a href="{{ link.url | relative_url }}"{% if link.url contains 'http' %} target="_blank" rel="noopener"{% endif %}>{{ link.label }}</a>{% endfor %}</div></div>
</section>
<section class="home-section"><p class="home-section__label">01 · Focus</p><h2>Research interests</h2>{% for interest in profile.research_interests %}- {{ interest }}
{% endfor %}</section>
<section class="home-section"><p class="home-section__label">02 · Work</p><h2>Selected publications</h2>{% assign selected_publications = profile.publications | where: "selected", true %}{% for publication in selected_publications limit: 3 %}<div class="publication-row"><span>{{ publication.year }}</span><div><strong>{{ publication.title }}</strong><p>{{ publication.venue }}</p></div></div>{% endfor %}<p><a href="{{ '/publications/' | relative_url }}">View all publications →</a></p></section>
<section class="home-section"><p class="home-section__label">03 · Research</p><h2>Projects</h2><div class="home-projects">{% for project in profile.projects %}<article><h3>{{ project.title }}</h3><p class="editable-list__summary">{{ project.summary }}</p><p>{{ project.description }}</p></article>{% endfor %}</div></section>
<section class="home-section"><p class="home-section__label">04 · Background</p><h2>Education</h2>{% for item in profile.education %}<div class="publication-row"><span>{{ item.period }}</span><div><strong>{{ item.degree }}</strong><p>{{ item.institution }} · {{ item.description }}</p></div></div>{% endfor %}</section>
<section class="home-section"><p class="home-section__label">05 · Academic life</p><h2>Activities & honors</h2>{% for group in profile.activities %}<h3>{{ group.category }}</h3>{% for item in group.items %}<div class="publication-row"><span>{{ item.year }}</span><div><strong>{{ item.title }}</strong><p>{{ item.description }}</p></div></div>{% endfor %}{% endfor %}{% if profile.honors.size > 0 %}{% for honor in profile.honors %}<div class="publication-row"><span>{{ honor.year }}</span><div><strong>{{ honor.title }}</strong><p>{{ honor.organization }}</p></div></div>{% endfor %}{% endif %}</section>
