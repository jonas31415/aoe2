from all_civs_available import all_civs_available
from aoe2_api import get_match_history_of_player_with_steam_id, filter_for_single_games, filter_for_double_games, \
    SingleMatch

COUNT_CIVS_IN_GAME = 42


class SinglePlayerStatistic:
    def __init__(self, win_counter_per_civ, successfull_against_civ, loss_counter_per_civ, lose_against_civ,
                 played_civ):
        self.played_civ = played_civ
        self.win_counter_per_civ = win_counter_per_civ
        self.successfull_against_civ = successfull_against_civ
        self.loss_counter_per_civ = loss_counter_per_civ
        self.lose_against_civ = lose_against_civ


def create_statistic_per_civ_single_player(games: list[SingleMatch]):
    win_counter_per_civ = [0] * COUNT_CIVS_IN_GAME
    successfull_against_civ = [0] * COUNT_CIVS_IN_GAME
    loss_counter_per_civ = [0] * COUNT_CIVS_IN_GAME
    lose_against_civ = [0] * COUNT_CIVS_IN_GAME
    played_civ = [0] * COUNT_CIVS_IN_GAME
    for game in games:
        played_civ[game.my_civ_index] += 1
        if game.won:
            win_counter_per_civ[game.my_civ_index] += 1
            successfull_against_civ[game.opponent_civ_index] += 1
        if not game.won:
            loss_counter_per_civ[game.my_civ_index] += 1
            lose_against_civ[game.opponent_civ_index] += 1

    return SinglePlayerStatistic(win_counter_per_civ, successfull_against_civ,
                                 loss_counter_per_civ, lose_against_civ, played_civ)

def plot_single_player_statistics(statistics: SinglePlayerStatistic):
    pass


if __name__ == "__main__":
    # steam_id = input("Enter steam id: ")
    steam_id = "76561198966904809"
    # steam_id = input("Enter your AOE2 name: ")
    player_name = "Lungaharing"
    all_games = get_match_history_of_player_with_steam_id(steam_id)
    single_games = filter_for_single_games(all_games, player_name)
    for game in single_games:
        print(f"Won: {game.won}, My Civ: {game.my_civ}, Opponent civ: {game.opponent_civ}")
    double_games = filter_for_double_games(all_games, player_name)
