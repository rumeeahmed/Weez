from AnalysisTools.weez_reader import Team, Player
from Tests.data_loader import DataLoader
from unittest import TestCase


class TestTeam(TestCase):
    """
    Object that tests the Team object.
    """

    def setUp(self) -> None:
        """
        Ensure that a Team object is instantiated, which needs a list of players
        with their processed stats.
        :return: None.
        """
        self.player_list = [
            Player('Captain Ahmed'), Player('The Golden God'), Player('Cheen')
        ]

        for player in self.player_list:
            loader = DataLoader(player.player_name)
            stats = loader.get_cleaned_matches()
            player.process_stats(stats)

        self.team = Team(self.player_list)

    def test_unit(self) -> None:
        """
        Test the properties of the Team object.
        :return: None.
        """
        assert self.team.player_list == self.player_list
        print(self.team.date)
        assert self.team.date is None

    def test_process_team_stats(self) -> None:
        """
        Process the Teams stats and check that the processed attributes are
        correct.
        :return: None.
        """
        self.team.process_team_stats()

        assert self.team.team_score == 40450
        assert self.team.team_kills == 30
        assert self.team.team_deaths == 60
        assert self.team.team_assists == 17
        assert self.team.team_damage == 16711
        assert self.team.team_damage_taken == 11868
        assert self.team.team_headshots == 3
        assert self.team.team_revives == 0
        assert self.team.team_teams_wiped == 0
        assert self.team.team_score_per_game == 6741.67
        assert self.team.team_kills_per_game == 5.0
        assert self.team.team_deaths_per_game == 10.0
        assert self.team.team_assists_per_game == 2.83
        assert self.team.team_damage_per_game == 2785.17
        assert self.team.team_damage_taken_per_game == 1978.0
        assert self.team.team_headshots_per_game == 0.5
        assert self.team.team_revives_per_game == 0
        assert self.team.teams_wiped_per_game == 0
        assert self.team.average_team_kd_per_game == 0.5
