import json
import os
from config import Config

class Database:
    @staticmethod
    def ensure_db_exists():
        os.makedirs(os.path.dirname(Config.DB_FILE), exist_ok=True)
        if not os.path.exists(Config.DB_FILE):
            with open(Config.DB_FILE, 'w') as f:
                json.dump({}, f)

    @staticmethod
    def load_db():
        Database.ensure_db_exists()
        try:
            with open(Config.DB_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Error: The file contains invalid JSON data.")
            return {}

    @staticmethod
    def save_db(db):
        with open(Config.DB_FILE, 'w') as f:
            json.dump(db, f, indent=2)

    @staticmethod
    def append_product(product_name, slot):
        db = Database.load_db()
        if product_name not in db:
            db[product_name] = []
        db[product_name].append({"product_name": product_name, "slot": slot})
        Database.save_db(db)