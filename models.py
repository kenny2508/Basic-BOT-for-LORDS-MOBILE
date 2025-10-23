import json
import os

CONFIG_DIR = "config"
USERS_FILE = os.path.join(CONFIG_DIR, "users.json")

class User:
    def __init__(self, user_id, name, guild=None, shield_time=0, resources=None):
        self.user_id = user_id
        self.name = name
        self.guild = guild
        self.shield_time = shield_time
        self.resources = resources or {
            "food": 0,
            "stone": 0,
            "wood": 0,
            "ore": 0,
            "gold": 0
        }

    def to_dict(self):
        return {
            "name": self.name,
            "guild": self.guild,
            "shield_time": self.shield_time,
            "resources": self.resources
        }

class Guild:
    def __init__(self, guild_id, name="Unknown Guild"):
        self.guild_id = guild_id
        self.name = name

class UserManager:
    @staticmethod
    def load_users():
        with open(USERS_FILE, "r") as f:
            data = json.load(f)
        users = {uid: User(uid, **info) for uid, info in data.items()}
        return users

    @staticmethod
    def save_users(users):
        data = {uid: user.to_dict() for uid, user in users.items()}
        with open(USERS_FILE, "w") as f:
            json.dump(data, f, indent=4)
