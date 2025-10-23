from core.engine import GameEngine

def main():
    engine = GameEngine()
    print("=== Lords Mobile Bot (Offline Mode) ===")
    user_id = input("Enter your user ID: ")

    while True:
        print("\nCommands:")
        print("1 - Check Shield | 2 - Renew Shield | 3 - Gather | 4 - Check Resources")
        print("5 - Join Guild | 6 - Guild Help | 7 - Battle | 8 - Hunt | 9 - Rally | 10 - Gather Tile | 0 - Exit")
        cmd = input("> ").strip()

        if cmd == "0":
            break
        elif cmd == "1":
            print(engine.check_shield(user_id))
        elif cmd == "2":
            print(engine.renew_shield(user_id))
        elif cmd == "3":
            r = input("Type: "); amt = int(input("Amt: "))
            print(engine.gather_resources(user_id, r, amt))
        elif cmd == "4":
            print(engine.get_resources(user_id))
        elif cmd == "5":
            gid = input("Guild ID: ")
            print(engine.join_guild(user_id, gid))
        elif cmd == "6":
            print(engine.send_guild_help(user_id))
        elif cmd == "7":
            print(engine.analyze_battle(user_id, {"kills": 2000, "losses": 150}))
        elif cmd == "8":
            lvl = int(input("Monster level: "))
            print(engine.hunt_monster(user_id, lvl))
        elif cmd == "9":
            rid = input("Rally ID: ")
            print(engine.join_rally(user_id, rid))
        elif cmd == "10":
            tile = input("Tile type: "); lvl = int(input("Level: "))
            print(engine.gather_tile(user_id, tile, lvl))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
