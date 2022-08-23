import requests

# api-endpoint-url
BASE_URL = "https://aoe2.net/api"


class SingleMatch:
    def __init__(self, my_civ, opponent_civ):
        self.my_civ = my_civ
        self.opponent_civ = opponent_civ
        

class DoubleMatch:
    def __init__(self, my_civ, team_partner_civ, opponent_1_civ, opponent_2_civ):
        self.my_civ = my_civ
        self.team_partner_civ = team_partner_civ
        self.opponent_1_civ = opponent_1_civ
        self.opponent_2_civ = opponent_2_civ
        
        
# sending get request and saving the response as response object
def get_match_history_of_player_with_steam_id(steam_id: str):
    r = requests.get(url=f"{BASE_URL}/player/matches?game=aoe2de&steam_id={steam_id}&count=100")
    data = r.json()
    return data


def extract_single_match_attributes_from_json(single_games):
    pass


def filter_for_single_games(all_games):
    single_games = []
    for game in all_games:
        if game['num_players'] == 2:
            single_games.append(game)
    return extract_single_match_attributes_from_json(single_games)


def extract_double_match_attributes_from_json(double_games):
    pass


def filter_for_double_games(all_games):
    double_games = []
    for game in all_games:
        if game['num_players'] == 4:
            double_games.append(game)
    return extract_double_match_attributes_from_json(double_games)
