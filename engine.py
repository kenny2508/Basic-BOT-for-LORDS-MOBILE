from functions import (
    shield_renewal,
    resource_manager,
    guild_assistant,
    battle_analyzer,
    hunting_manager,
)
from core.models import UserManager

class GameEngine:
    def __init__(self):
        self.users = UserManager.load_users()

    def save(self):
        UserManager.save_users(self.users)

    def get_user(self, user_id):
        return self.users.get(user_id)

    # --- Wrappers around module functions ---
    def check_shield(self, user_id):
        return shield_renewal.check_shield_status(user_id)

    def renew_shield(self, user_id):
        return shield_renewal.renew_shield(user_id)

    def gather_resources(self, user_id, rtype, amount):
        return resource_manager.gather_resources(user_id, rtype, amount)

    def get_resources(self, user_id):
        return resource_manager.get_resource_status(user_id)

    def join_guild(self, user_id, guild_id):
        return guild_assistant.join_guild(user_id, guild_id)

    def send_guild_help(self, user_id):
        return guild_assistant.send_guild_help(user_id)

    def analyze_battle(self, user_id, data):
        return battle_analyzer.analyze_attack_report(user_id, data)

    def hunt_monster(self, user_id, level):
        return hunting_manager.hunt_monster(user_id, level)

    def join_rally(self, user_id, rally_id):
        return hunting_manager.join_rally(user_id, rally_id)

    def gather_tile(self, user_id, tile_type, level):
        return hunting_manager.gather_tile(user_id, tile_type, level)
