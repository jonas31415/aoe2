import requests

# api-endpoint-url
from all_civs_available import all_civs_available

BASE_URL = "https://aoe2.net/api"


class SingleMatch:
    def __init__(self, won, my_civ, my_civ_index, opponent_civ, opponent_civ_index):
        self.won = won
        self.my_civ = my_civ
        self.my_civ_index = my_civ_index
        self.opponent_civ = opponent_civ
        self.opponent_civ_index = opponent_civ_index
        

class DoubleMatch:
    def __init__(self, my_civ, team_partner_civ, opponent_1_civ, opponent_2_civ):
        self.my_civ = my_civ
        self.team_partner_civ = team_partner_civ
        self.opponent_1_civ = opponent_1_civ
        self.opponent_2_civ = opponent_2_civ
        
        
# sending get request and saving the response as response object
def get_match_history_of_player_with_steam_id(steam_id: str):
    r = requests.get(url=f"{BASE_URL}/player/matches?game=aoe2de&steam_id={steam_id}&count=1000")
    data = r.json()
    return data


def extract_single_match_attributes_from_json(single_games, my_aoe_name):
    single_games_with_relevant_attributes = []
    my_civ = ''
    my_civ_index = 0
    opponent_civ = ''
    opponent_civ_index = 0
    won = False
    for game in single_games:
        falsy = False
        for player in game['players']:
            if player['civ'] > 42:
                falsy = True
                continue
            if player['name'] == my_aoe_name:
                my_civ = all_civs_available[player['civ']-1]
                my_civ_index = player['civ']-1
                won = player['won']
            else:
                opponent_civ = all_civs_available[player['civ']-1]
                opponent_civ_index = player['civ']-1
        if not falsy:
            single_games_with_relevant_attributes.append(SingleMatch(won, my_civ, my_civ_index,
                                                                     opponent_civ, opponent_civ_index))
    return single_games_with_relevant_attributes


def filter_for_single_games(all_games, my_aoe_name):
    single_games = []
    for game in all_games:
        if game['num_players'] == 2:
            single_games.append(game)
    return extract_single_match_attributes_from_json(single_games, my_aoe_name)


def extract_double_match_attributes_from_json(double_games, my_aoe_name):
    # TODO
    pass


def filter_for_double_games(all_games, my_aoe_name):
    double_games = []
    for game in all_games:
        if game['num_players'] == 4:
            double_games.append(game)
    return extract_double_match_attributes_from_json(double_games, my_aoe_name)
