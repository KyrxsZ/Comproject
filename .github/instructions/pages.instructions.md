---
applyTo: "pages/**"
---
# Rules for files in pages/

- A page file has `TITLE`, `def build()` (or `def build(query)`), and optionally `def handle(form)`.
  Nothing else is needed: no imports from flask, no `@app.route`, no `request`.
- Data comes from `storage.load()`; write back only with `storage.save(items)`. A page may also
  compute from user input (`build(query)` for a calculator page) — that is fine.
- Keep `build()` under about 30 lines. If it grows, split a helper `def` — that is a
  function point in the grade.
- Prefer a plain `for` loop with an `if` inside over comprehensions or `filter`/`map`.
- Sorting: show the selection loop from `catalog/ranking/page.py` before mentioning `sorted()`.
- `build()` must return a dict. Every key becomes a variable in `templates/<same name>.html`.
  A key named `notice` is shown as the yellow banner.
- Python's standard library is allowed (`datetime`, `random`, `math`). Packages that need
  `pip install` are not (Flask is already there).
- Before writing new code, check whether `catalog/` already has this page type and start from it:
  list, form, detail, search, stats, ranking, calculator, cart, gallery, text.

## Form pitfalls — tell the student about these when they write `handle(form)`
- `form` is a dict of **strings**. Use `form.get("x", "")` — a radio/checkbox that is not ticked,
  or an input that is `disabled`, sends **no key** and `form["x"]` raises `KeyError`. Use
  `readonly` instead of `disabled` for fields that must be submitted.
- Numbers: `int()` / `float()` inside `try` / `except ValueError`. `float("nan")` passes — copy
  `read_number()` from `catalog/form/page.py`.
- Return a short message string; `app.py` redirects back to the same page and shows it.
- Several buttons on one page = several small `<form method="post">` each sending a hidden
  `action` (and a row number stamped in `build()` as `item["no"]`), and one `handle()` that
  branches with `if form.get("action") == "...":` — see `catalog/form` and `catalog/cart`.
- Uploads: form has `enctype="multipart/form-data"`; `app.py` saves the file into `static/img/`
  and puts the saved file name in `form["photo"]` (`""` if none / not an image) — see `catalog/gallery`.
- **State between pages** (a cart, a selection, a login) cannot live in a variable at the top of
  the file — `app.py` reloads page files on every request. Store a flag in `data.json` rows
  (`"picked": true`) — see `catalog/cart`.
- Never trust the form: validate every value before saving.
- When the student's page crashes, the site shows the traceback on the "ยังไม่พร้อม" page —
  ask them to paste it, then explain it.
- Never create or edit `team.py` logic unless the student explicitly wants to customise the team page.
