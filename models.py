"""models.py — ★ your one class lives here.

TODO: rename Item to fit your project (Book, Player, Expense, Room, Equipment ...),
give it the fields you keep in data.json, and one method that does something useful.

A page can turn a row from data.json into an object like this:

    import models
    item = models.Item(row["name"], row["price"])
    item.describe()
"""


class Restaurant:
    def __init__(self, row):
        self.id = row.get("id", "")
        self.name = row.get("name", "")
        self.category = row.get("category", "")
        self.status = row.get("status", "closed")
        self.rating = row.get("rating", 0)
        self.review_count = row.get("review_count", 0)
        self.description = row.get("description", "")
        self.location = row.get("location", "")
        self.opening_hours = row.get("opening_hours", "")
        self.image = row.get("image", "placeholder.svg")
        self.menus = row.get("menus", [])
        self.reviews = row.get("reviews", [])

    def status_label(self):
        labels = {
            "open": "เปิดอยู่",
            "closed": "ปิดอยู่",
            "temporary": "ปิดชั่วคราว",
        }
        return labels.get(self.status, "ไม่ทราบสถานะ")
