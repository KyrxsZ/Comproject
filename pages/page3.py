"""Public statistics calculated from restaurant reviews and menus."""
import firebase_store

TITLE = "สถิติ"


def build():
    restaurants = firebase_store.load_restaurants()
    total_reviews = 0
    total_rating = 0
    open_count = 0
    distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    availability = {"available": 0, "almost": 0, "sold_out": 0, "temporary": 0}
    for restaurant in restaurants:
        if restaurant.get("status") == "open":
            open_count = open_count + 1
        reviews = restaurant.get("reviews", [])
        total_reviews = total_reviews + len(reviews)
        for review in reviews:
            rating = review.get("rating", 0)
            if rating in distribution:
                distribution[rating] = distribution[rating] + 1
            total_rating = total_rating + rating
        for menu in restaurant.get("menus", []):
            status = menu.get("availability", "temporary")
            if status in availability:
                availability[status] = availability[status] + 1
    average = round(total_rating / total_reviews, 1) if total_reviews > 0 else 0
    bars = []
    for rating in range(5, 0, -1):
        percent = int(distribution[rating] * 100 / total_reviews) if total_reviews > 0 else 0
        bars.append({"label": str(rating) + " ดาว", "count": distribution[rating], "percent": percent})
    return {"restaurants": restaurants, "total": len(restaurants), "open_count": open_count, "total_reviews": total_reviews, "average": average, "bars": bars, "availability": availability, "backend": firebase_store.backend_name()}
