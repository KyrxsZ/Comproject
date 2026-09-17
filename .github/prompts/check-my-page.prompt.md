---
mode: ask
description: "Review my page against the page contract and the grading foundations"
---
Review the page I have open (its `pages/pageN.py` and `templates/pageN.html`). Answer as a
short checklist with ✓ / ✗ and one line each:

- `TITLE` set and meaningful
- `build()` returns a dict, reads data only with `storage.load()`
- the template extends `base.html`, uses only variables that `build()` returns
- no leftover `TODO` in either file
- which foundations this page shows: if/else · loop · function · class (say which lines)
- anything a first-year could simplify (one suggestion at most)
- is every line something I could explain to my teacher? If a line looks copied without
  understanding, ask me to explain it.

Do not rewrite the files. End with: `python check_project.py` and the commit command.
