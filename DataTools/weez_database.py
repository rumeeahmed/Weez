from AnalysisTools.weez_reader import Player, Team
from firebase_admin import credentials, firestore
from AnalysisTools.weez_awards import WeezAwards
import firebase_admin


class WeezDatabase:
    """
    Object that handles data storage into Firebase.
    """

    def __init__(self):
        self._initialize_app()

    def _initialize_app(self) -> None:
        """
        Get the credentials, initialise the app and create a connection to the
        Firestore database.
        :return: None.
        """
        if not firebase_admin._apps:
            cred = credentials.Certificate(
                '/Users/rumeeahmed/Documents/Weez/DataTools/service_key.json'
            )
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def _add_player(self, player_list: list[Player]) -> None:
        """
        Add the players to the players' collection.
        :param player_list: a list containing player objects.
        :return: None
        """
        for player in player_list:
            player_dict = {"player": player.player_name}
            self.db.collection('players').document(player.player_name).set(
                player_dict
            )

    def add_games(self, player_list: list[Player]) -> None:
        """
        Add a game session to the Firebase database under the `games`
        collection.
        :param player_list: a list containing player objects.
        :return: None.
        """
        self._add_player(player_list)
        for player in player_list:
            game = {
                'games_played': player.games_played,
                'score': player.score,
                'kills': player.kills,
                'deaths': player.deaths,
                'assists': player.assists,
                'damage': player.damage,
                'damage_taken': player.damage_taken,
                'kd': player.kd,
                'headshots': player.headshots,
                'revives': player.revives,
                'teams_wiped': player.teams_wiped,
                'distance_travelled': player.distance_travelled,
                'time_moving_percent': player.time_moving,
                'crates_opened': player.crates_opened,
                'shop_buys': player.shop_buys,
                'gn': player.judge,
            }
            self.db.collection('games').document(player.date).collection(
                player.player_name
            ).document('stats').set(game)

    def add_awards(self, awards: WeezAwards) -> None:
        """
        Add the awards generated from a session to the Firebase database under
        the`awards` collection.
        :param awards: an instance of the WeezAwards object.
        :return: None
        """
        data = {
            'bullet_bitch': awards.bullet_bitch,
            'medic': awards.medic,
            'head_master': awards.head_master,
            'top_assister': awards.top_assister,
            'team_lover': awards.team_lover,
            'team_hater': awards.team_hater,
            'lethal_killer': awards.lethal_killer,
            'least_lethal_killer': awards.least_lethal_killer,
            'tank': awards.tank,
            'gummy_bear': awards.gummy_bear,
            'team_demolisher': awards.team_demolisher,
            'weary_traveller': awards.weary_traveller,
            'big_spender': awards.big_spender,
            'hungry_bitch': awards.hungry_bitch,
            'pussio': awards.pussio,
        }
        self.db.collection('awards').document(awards.date).set(data)

    def add_team(self, team: Team) -> None:
        """
        Add the team stats generated from a session to the Firebase database
        under the`awards` collection.
        :param team: an instance of the Team object.
        :return: None
        """
        self._add_total_team_stats(team)
        self._add_team_stats_per_game(team)

    def _add_total_team_stats(self, team: Team) -> None:
        """
        Add the total team stats per session into the Firebase database under
        the `total_team_stats` Collection.
        :param team: an instance of the Team object.
        :return: None.
        """
        data = {
            'team_score': team.team_score,
            'team_kills': team.team_kills,
            'team_deaths': team.team_deaths,
            'team_assists': team.team_assists,
            'team_damage': team.team_damage,
            'team_damage_taken': team.team_damage_taken,
            'team_headshots': team.team_headshots,
            'team_revives': team.team_revives,
            'team_teams_wiped': team.team_teams_wiped,
            'team_kd_average': team.average_team_kd,
        }
        self.db.collection('total_team_stats').document(team.date).set(data)

    def _add_team_stats_per_game(self, team: Team) -> None:
        """
        Add the average team stats per game into the Firebase database under
        the `team_stats_per_game` collection.
        :param team: an instance of the WeezAwards object.
        :return: None.
        """
        data = {
            'team_score_per_game': team.team_score_per_game,
            'team_kills_per_game': team.team_kills_per_game,
            'team_deaths_per_game': team.team_deaths_per_game,
            'team_assists_per_game': team.team_assists_per_game,
            'team_damage_per_game': team.team_damage_per_game,
            'team_damage_taken_per_game': team.team_damage_taken_per_game,
            'team_headshots_per_game': team.team_headshots_per_game,
            'team_revives_per_game': team.team_revives_per_game,
            'teams_wiped_per_game': team.teams_wiped_per_game,
            'team_kd_average_per_game': team.average_team_kd_per_game,
        }
        self.db.collection('team_stats_per_game').document(team.date).set(data)
