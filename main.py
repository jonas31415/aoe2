from aoe2_api import get_match_history_of_player_with_steam_id, filter_for_single_games, filter_for_double_games

if __name__ == "__main__":
    # steam_id = input("Enter steam id: ")
    steam_id = "76561198966904809"
    # steam_id = input("Enter your AOE2 name: ")
    player_name = "Lungaharing"
    all_games = get_match_history_of_player_with_steam_id(steam_id)
    print(filter_for_single_games(all_games))
    # print(filter_for_double_games)
