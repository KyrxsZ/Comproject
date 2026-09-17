"""Shopkeeper view: create restaurants and manage menus."""
import re

import firebase_store

TITLE = "ผู้ดูแลร้าน"


def build(query):
    restaurants = firebase_store.load_restaurants()
    selected_id = query.get("id", "")
    selected = None
    for restaurant in restaurants:
        if restaurant.get("id") == selected_id:
            selected = restaurant
    if selected is None and len(restaurants) > 0:
        selected = restaurants[0]
    return {"restaurants": restaurants, "selected": selected, "backend": firebase_store.backend_name()}


def make_id(name, restaurants):
    base = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-") or "restaurant"
    candidate = base
    number = 2
    used = []
    for restaurant in restaurants:
        used.append(restaurant.get("id", ""))
    while candidate in used:
        candidate = base + "-" + str(number)
        number = number + 1
    return candidate


def handle(form):
    restaurants = firebase_store.load_restaurants()
    action = form.get("action", "")
    if action == "create":
        name = form.get("name", "").strip()
        if name == "":
            return "กรุณากรอกชื่อร้าน"
        restaurants.append({"id": make_id(name, restaurants), "name": name, "category": form.get("category", "").strip(), "status": form.get("status", "closed"), "rating": 0, "review_count": 0, "description": form.get("description", "").strip(), "location": form.get("location", "").strip(), "opening_hours": form.get("opening_hours", "").strip(), "image": form.get("cover", "") or "placeholder.svg", "menus": [], "reviews": []})
        firebase_store.save_restaurants(restaurants)
        return "สร้างร้านอาหารแล้ว"
    for restaurant in restaurants:
        if restaurant.get("id") != form.get("restaurant_id", ""):
            continue
        if action == "restaurant_status":
            restaurant["status"] = form.get("status", "closed")
        elif action == "add_menu":
            name = form.get("menu_name", "").strip()
            try:
                price = float(form.get("price", "0"))
            except ValueError:
                return "ราคาต้องเป็นตัวเลข"
            if name == "" or price < 0:
                return "กรุณากรอกชื่อเมนูและราคาที่ถูกต้อง"
            restaurant.setdefault("menus", []).append({"id": make_id(name, restaurant.get("menus", [])), "name": name, "description": form.get("menu_description", "").strip(), "price": price, "category": form.get("menu_category", "").strip(), "availability": form.get("availability", "available"), "image": form.get("photo", "") or "placeholder.svg", "display_order": len(restaurant.get("menus", [])) + 1})
        elif action == "availability":
            for menu in restaurant.get("menus", []):
                if menu.get("id") == form.get("menu_id", ""):
                    menu["availability"] = form.get("availability", "available")
        firebase_store.save_restaurants(restaurants)
        return "อัปเดตข้อมูลร้านแล้ว"
    return "ไม่พบร้านอาหารนี้"
