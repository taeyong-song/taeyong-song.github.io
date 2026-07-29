---
layout: page
title: home
permalink: /
nav: true
nav_order: 1
---
{% assign profile = site.data.profile %}
<style>.post-header { display: none; }</style>
<div class="personal-home">
<aside class="personal-profile">
{% if profile.identity.photo %}<img class="personal-profile__photo" src="{{ profile.identity.photo | relative_url }}" alt="Portrait of {{ profile.identity.name }}">{% else %}<div class="personal-profile__placeholder" aria-label="Portrait placeholder">TYS</div>{% endif %}
<p class="personal-profile__role">{{ profile.identity.role }} · {{ profile.identity.field }}</p><h1>{{ profile.identity.name }}</h1><p class="personal-profile__affiliation">{{ profile.identity.department }}<br>{{ profile.identity.affiliation }}</p>
<div class="personal-profile__bio">{% for paragraph in profile.about %}<p>{{ paragraph }}</p>{% endfor %}</div>
<nav class="personal-profile__links" aria-label="Professional profiles">{% for link in profile.links %}<a href="{{ link.url | relative_url }}"{% if link.url contains 'http' %} target="_blank" rel="noopener"{% endif %}>{{ link.label }}</a>{% endfor %}</nav>
</aside>
<main class="personal-record">
<section class="record-intro"><p class="home-section__label">Research profile</p><h2>Building intelligence grounded in physical meaning.</h2><p>I study how building models can remain interpretable, transferable, and useful for decisions when operational data are limited.</p></section>
<section class="home-section"><p class="home-section__label">01 · Research focus</p><h2>Research interests</h2><div class="interest-grid">{% for interest in profile.research_interests %}<div><span>0{{ forloop.index }}</span><p>{{ interest }}</p></div>{% endfor %}</div></section>
<section class="home-section"><p class="home-section__label">02 · Publications</p><h2>Selected work</h2>{% assign selected_publications = profile.publications | where: "selected", true %}{% for publication in selected_publications limit: 3 %}<div class="publication-row"><span>{{ publication.year }}</span><div><strong>{% if publication.doi %}<a href="{{ publication.doi }}" target="_blank" rel="noopener">{{ publication.title }}</a>{% else %}{{ publication.title }}{% endif %}</strong><p>{{ publication.venue }}</p></div></div>{% endfor %}<p class="section-link"><a href="{{ '/publications/' | relative_url }}">All publications →</a></p></section>
<section class="home-section"><p class="home-section__label">03 · Projects</p><h2>Current research directions</h2><div class="home-projects">{% for project in profile.projects %}<article><span>0{{ forloop.index }}</span><h3>{{ project.title }}</h3><p class="editable-list__summary">{{ project.summary }}</p><p>{{ project.description }}</p></article>{% endfor %}</div></section>
<section class="home-section"><p class="home-section__label">04 · Career</p><h2>Education</h2>{% for item in profile.education %}<div class="publication-row"><span>{{ item.period }}</span><div><strong>{{ item.degree }}</strong><p>{{ item.institution }} · {{ item.description }}</p></div></div>{% endfor %}</section>
<section class="home-section"><p class="home-section__label">05 · Activities</p><h2>Academic activities & honors</h2>{% for group in profile.activities %}<h3>{{ group.category }}</h3>{% for item in group.items %}<div class="publication-row"><span>{{ item.year }}</span><div><strong>{{ item.title }}</strong><p>{{ item.description }}</p></div></div>{% endfor %}{% endfor %}{% if profile.honors.size > 0 %}{% for honor in profile.honors %}<div class="publication-row"><span>{{ honor.year }}</span><div><strong>{{ honor.title }}</strong><p>{{ honor.organization }}</p></div></div>{% endfor %}{% endif %}</section>
</main></div>
