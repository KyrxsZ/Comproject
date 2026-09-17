---
mode: ask
description: "Start a new page: pick a catalog type, copy it, adapt it to our data"
---
I want to build a page for this project. Help me step by step, as a tutor:

1. Ask me which page number (page1 / page2 / page3 / page4) and what the page should show.
2. Look at `data.json` and tell me which fields we have.
3. Recommend ONE type from `catalog/` (list, form, detail, search, stats, ranking, calculator,
   cart, gallery, text) and say why in one sentence. If two types together fit better
   (for example cards from `cart` plus the search box from `search`), say which one to start
   from and what to borrow from the other. Remind me that `text` does not count as one of
   pages 1–3 because it has no Python work (a loop or an if over data).
4. Tell me the two copy steps: `catalog/<type>/page.py` → `pages/pageN.py` and
   `catalog/<type>/page.html` → `templates/pageN.html`.
5. Then list, as a short checklist, exactly which lines I must change so the page uses OUR
   field names and OUR title. Do not rewrite the whole file for me.
6. If the page has a form, remind me of the form pitfalls in `.github/instructions/pages.instructions.md`
   (`form.get`, numbers through `try/except`, hidden `action` for several buttons, state in `data.json`).
7. Finish with what to run: `run.bat` (or `python app.py`), open the page, `check.bat`
   (or `python check_project.py`), and the commit command `git commit -m "pageN: ..."`.
