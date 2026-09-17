---
applyTo: "templates/**"
---
# Rules for files in templates/

- Every page template starts with `{% extends "base.html" %}` and puts its content inside
  `{% block content %} … {% endblock %}`. Do not add `<html>`, `<head>` or `<body>`.
- `base.html` and `_not_built.html` are GIVEN — never edit them. The header, logo, menu and
  footer come from there.
- Only Jinja and plain HTML/CSS: `{{ variable }}`, `{% for item in items %}`, `{% if … %}`,
  `{% for key, value in some_dict.items() %}`. Variables are the keys of the dict returned by
  `build()` in the matching `pages/*.py`, plus `title`.
- Use the classes that already exist in `static/style.css` (see the table in `docs/tools/jinja.md`):
  `table`, `.stat-grid/.stat`, `.panel`, `.two-col`, `.card-grid/.item-card`, `.badge`, `.pills`,
  `.bar-row/.bar-track/.bar-fill`, `.chart/.col`, `.progress`, `.btn`, `.field`, `.empty`, `.gallery`.
  New CSS goes at the bottom of `static/style.css` under "your own styles".
- Charts: compute the percent in Python, then `style="width: {{ p }}%"` or `style="height: {{ p }}%"`.
  Never scale pixels from raw values.
- Forms: `<form method="post">` sends to the same page → `handle(form)`. `<form method="get">`
  puts the fields in the URL → `build(query)`. Input `name="x"` becomes `form["x"]` / `query["x"]`.
  File upload needs `enctype="multipart/form-data"`.
- Images go in `static/img/` and are referenced with `{{ url_for('static', filename='img/x.jpg') }}`.
  13 sample SVG icons are already there (arduino, book, mouse, …).
- **JavaScript policy:** not needed for this project. If the topic truly requires it (a game, an
  animation), put it in `{% block scripts %} … {% endblock %}` after the content block, or in
  `static/js/pageN.js`. JavaScript earns no points and the student is not asked to explain it
  line by line, but the page must still have real Python work (a loop or an if over data) to
  count as one of pages 1–3. Keep it as small as possible and never load external libraries.
- Thai text is fine everywhere; keep the file UTF-8.
