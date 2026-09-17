"""Student view: discover restaurants, menus, and reviews."""
import hashlib
import re
from datetime import date

import firebase_store
import models

TITLE = "ผู้ใช้"


def restaurant_view(row):
    item = dict(row)
    restaurant = models.Restaurant(row)
    item["status_label"] = restaurant.status_label()
    item["reviews"] = list(row.get("reviews", []))
    item["menus"] = list(row.get("menus", []))
    return item


def build(query):
    keyword = query.get("q", "").strip().lower()
    status = query.get("status", "")
    selected_id = query.get("id", "")
    restaurants = []
    categories = []
    selected = None
    for row in firebase_store.load_restaurants():
        if row.get("category", "") not in categories:
            categories.append(row.get("category", ""))
        text = row.get("name", "") + " " + row.get("category", "")
        if (keyword == "" or keyword in text.lower()) and (status == "" or row.get("status") == status):
            restaurants.append(restaurant_view(row))
        if row.get("id") == selected_id:
            selected = restaurant_view(row)
    return {"restaurants": restaurants, "selected": selected, "categories": categories, "backend": firebase_store.backend_name()}


def handle(form):
    if form.get("action", "") != "review":
        return "ไม่พบคำสั่งที่ต้องการ"
    student_id = form.get("student_id", "").strip()
    if re.fullmatch(r"[0-9]{11}", student_id) is None:
        return "รหัสนักศึกษาต้องเป็นตัวเลข 11 หลัก"
    try:
        rating = int(form.get("rating", "0"))
    except ValueError:
        return "กรุณาเลือกคะแนน 1 ถึง 5 ดาว"
    if rating < 1 or rating > 5:
        return "กรุณาเลือกคะแนน 1 ถึง 5 ดาว"
    restaurants = firebase_store.load_restaurants()
    student_hash = hashlib.sha256(student_id.encode("utf-8")).hexdigest()
    for restaurant in restaurants:
        if restaurant.get("id") == form.get("restaurant_id", ""):
            reviews = restaurant.setdefault("reviews", [])
            for review in reviews:
                if review.get("student_id_hash") == student_hash:
                    return "รหัสนี้เคยรีวิวร้านนี้แล้ว"
            reviews.append({"student_id_hash": student_hash, "rating": rating, "comment": form.get("comment", "").strip(), "reviewer_display": "นักศึกษา ****" + student_id[-2:], "created_at": str(date.today())})
            restaurant["review_count"] = len(reviews)
            total = 0
            for review in reviews:
                total = total + review.get("rating", 0)
            restaurant["rating"] = round(total / len(reviews), 1)
            firebase_store.save_restaurants(restaurants)
            return "บันทึกรีวิวแล้ว"
    return "ไม่พบร้านอาหารนี้"
