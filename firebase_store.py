"""Small Firestore adapter with a local JSON fallback for classroom development."""
import json
import os
import glob

import storage

_db = None
_checked = False


def _service_account_setting():
    configured = os.environ.get("FIREBASE_SERVICE_ACCOUNT", "")
    if configured != "":
        return configured

    here = os.path.dirname(os.path.abspath(__file__))
    search_dirs = [here, os.path.dirname(here), os.path.dirname(os.path.dirname(here))]
    names = ["firebase-service-account.json", "serviceAccountKey.json", "*-service-account.json", "*-firebase-adminsdk-*.json"]
    for directory in search_dirs:
        for name in names:
            matches = glob.glob(os.path.join(directory, name))
            if matches:
                return matches[0]
    return ""


def _connect():
    """Connect once when Firebase credentials are configured."""
    global _db, _checked
    if _checked:
        return _db
    _checked = True

    service_account = _service_account_setting()
    if service_account == "":
        return None

    try:
        import firebase_admin
        from firebase_admin import credentials, firestore

        if not firebase_admin._apps:
            if os.path.exists(service_account):
                certificate = credentials.Certificate(service_account)
            else:
                certificate = credentials.Certificate(json.loads(service_account))
            firebase_admin.initialize_app(certificate)
        _db = firestore.client()
    except Exception:
        _db = None
    return _db


def is_connected():
    return _connect() is not None


def load_restaurants():
    """Read restaurants from Firestore, or local data while Firebase is offline."""
    database = _connect()
    if database is None:
        return storage.load()

    restaurants = []
    for document in database.collection("restaurants").stream():
        restaurant = document.to_dict()
        restaurant["id"] = document.id
        menus = []
        for menu in document.reference.collection("menus").stream():
            item = menu.to_dict()
            item["id"] = menu.id
            menus.append(item)
        restaurant["menus"] = menus
        restaurants.append(restaurant)
    return restaurants


def save_restaurants(restaurants):
    """Save restaurant documents and their menu subcollections."""
    database = _connect()
    if database is None:
        storage.save(restaurants)
        return

    for restaurant in restaurants:
        restaurant_id = restaurant.get("id", "")
        if restaurant_id == "":
            restaurant_id = database.collection("restaurants").document().id
            restaurant["id"] = restaurant_id
        menus = restaurant.get("menus", [])
        document_data = dict(restaurant)
        document_data.pop("id", None)
        document_data.pop("menus", None)
        database.collection("restaurants").document(restaurant_id).set(document_data)
        menu_collection = database.collection("restaurants").document(restaurant_id).collection("menus")
        for menu in menus:
            menu_id = menu.get("id", "")
            if menu_id == "":
                menu_id = menu_collection.document().id
            menu_data = dict(menu)
            menu_data.pop("id", None)
            menu_collection.document(menu_id).set(menu_data)


def backend_name():
    if is_connected():
        return "Firebase Firestore"
    return "data.json (โหมดพัฒนา)"
