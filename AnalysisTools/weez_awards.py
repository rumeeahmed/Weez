from AnalysisTools.weez_reader import Player


class WeezAwards:
    """
    Object that calculates various award metrics for a Player.
    """

    def __init__(self, player_list: list[Player]):
        """

        :param player_list: a list object containing Player objects.
        """
        self.player_list = player_list
        self.pussio = 'Cheen'
        self.date = player_list[0].date

    def __repr__(self) -> str:
        return f'WeezAwards({self.player_list})'

    def _get_bullet_bitch(self) -> None:
        """
        Calculate the Player who has absorbed the most damage in the session.
        :return: None.
        """
        self.bullet_bitch = None
        max_damage = 0

        for player in self.player_list:
            if player.damage_taken > max_damage:
                self.bullet_bitch = player.player_name
                max_damage = player.damage_taken

    def _get_medic(self) -> None:
        """
        Calculate the Player with the most revives in the session.
        :return: None.
        """
        self.medic = None
        max_revives = 0

        for player in self.player_list:
            if player.revives > max_revives:
                self.medic = player.player_name
                max_revives = player.revives

    def _get_head_master(self) -> None:
        """
        Calculate the Player with the most headshots in the session.
        :return: None.
        """
        self.head_master = None
        max_headshots = 0

        for player in self.player_list:
            if player.headshots > max_headshots:
                self.head_master = player.player_name
                max_headshots = player.headshots

    def _get_assister(self) -> None:
        """
        Calculate the Player with the most assists in the session.
        :return: None.
        """
        self.top_assister = None
        max_assists = 0

        for player in self.player_list:
            if player.assists > max_assists:
                self.top_assister = player.player_name
                max_assists = player.assists

    def _get_team_lover_and_hater(self) -> None:
        """
        Calculate the Player that loves the team (the highest score) and the
         Player that hates the team (the lowest score).
        :return: None.
        """
        self.team_lover = None
        self.team_hater = None
        max_score = 0
        min_score = 100000

        for player in self.player_list:
            if player.score > max_score:
                self.team_lover = player.player_name
                max_score = player.score
            if player.score < min_score:
                self.team_hater = player.player_name
                min_score = player.score

    def _get_lethality(self) -> None:
        """
        Calculate the most and least lethal Player. Lethality is calculated by
        damage per kill.
        :return:None.
        """
        self.lethal_killer = None
        self.least_lethal_killer = None
        max_lethality = 0
        min_lethality = 100000

        for player in self.player_list:
            ratio = player.damage / player.kills
            if ratio > max_lethality:
                self.least_lethal_killer = player.player_name
                max_lethality = ratio
            if ratio < min_lethality:
                self.lethal_killer = player.player_name
                min_lethality = ratio

    def _get_tank(self) -> None:
        """
        Calculate the Player who requires the most damage for a death and the
        Player that takes the least damage per death.
        :return: None.
        """
        self.tank = None
        self.gummy_bear = None
        max_value = 0
        min_value = 100000

        for player in self.player_list:
            ratio = player.damage_taken / player.deaths
            if ratio > max_value:
                self.tank = player.player_name
                max_value = ratio
            if ratio < min_value:
                self.gummy_bear = player.player_name
                min_value = ratio

    def _get_team_demolisher(self) -> None:
        """
        Calculate the Player with the most team wipes in the session.
        :return: None.
        """
        self.team_demolisher = None
        max_team_wipes = 0

        for player in self.player_list:
            if player.teams_wiped > max_team_wipes:
                self.team_demolisher = player.player_name
                max_team_wipes = player.teams_wiped

    def _get_weary_traveller(self) -> None:
        """
        Calculate the Player with the most team wipes in the session.
        :return: None.
        """
        self.weary_traveller = None
        max_distance = 0

        for player in self.player_list:
            if player.distance_travelled > max_distance:
                self.weary_traveller = player.player_name
                max_distance = player.distance_travelled

    def _get_big_spender(self) -> None:
        """
        Calculate the Player with the most team wipes in the session.
        :return: None.
        """
        self.big_spender = None
        shop_buys = 0

        for player in self.player_list:
            if player.shop_buys > shop_buys:
                self.big_spender = player.player_name
                shop_buys = player.shop_buys

    def _get_hungry_bitch(self) -> None:
        """
        Calculate the Player with the most team wipes in the session.
        :return: None.
        """
        self.hungry_bitch = None
        crates_opened = 0

        for player in self.player_list:
            if player.crates_opened > crates_opened:
                self.hungry_bitch = player.player_name
                crates_opened = player.crates_opened

    def process_player_stats(self) -> None:
        """
        Method that calls all the private methods to produce the awards.
        :return: None.
        """
        self._get_bullet_bitch()
        self._get_medic()
        self._get_head_master()
        self._get_assister()
        self._get_team_lover_and_hater()
        self._get_lethality()
        self._get_tank()
        self._get_team_demolisher()
        self._get_weary_traveller()
        self._get_big_spender()
        self._get_hungry_bitch()

    def show_player_results(self) -> str:
        """
        Produce a string that shows the entire results of the awards.
        :return: String object that contains the awards.
        """
        results = f'{self.bullet_bitch} is the bullet bitch\n' \
                  f'{self.medic} is the medic\n' \
                  f'{self.head_master} is the headmaster\n' \
                  f'{self.top_assister} is the top assister\n' \
                  f'{self.team_lover} loves the team\n' \
                  f'{self.team_hater} hates the team\n' \
                  f'{self.lethal_killer} is the lethal killer\n' \
                  f'{self.least_lethal_killer} is the least lethal killer\n' \
                  f'{self.tank} is the tank\n' \
                  f'{self.gummy_bear} is the gummy bear\n' \
                  f'{self.team_demolisher} is the team demolisher\n' \
                  f'{self.weary_traveller} is the weary traveller\n' \
                  f'{self.big_spender} is the big spender\n' \
                  f'{self.hungry_bitch} is the hungry bitch\n' \
                  f'{self.pussio} is the pussi o\n'
        return results
