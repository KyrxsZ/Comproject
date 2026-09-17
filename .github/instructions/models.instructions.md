---
applyTo: "models.py"
---
# Rules for models.py

- Exactly one class. Rename `Item` to fit the topic (Book, Player, Expense, Equipment …).
- `__init__` stores each field of a `data.json` row as an attribute with the same name.
- One more method that does something useful with the fields and returns a value
  (a sentence, a total, a yes/no). No `@property`, no `@staticmethod`, no inheritance,
  no dataclass, no type hints.
- Remove every `TODO` comment when done — the grader gives 0/9 while a TODO remains.
- Show how a page uses it: `models.Item(row["name"], row["price"]).describe()` — see
  `catalog/detail/page.py`.
