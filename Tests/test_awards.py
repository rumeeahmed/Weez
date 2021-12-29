from AnalysisTools.weez_awards import WeezAwards
from AnalysisTools.weez_reader import Player
from Tests.data_loader import DataLoader
from unittest import TestCase


class TestWeezAwards(TestCase):
    """
    Object that tests the WeezAwards object
    """

    def setUp(self) -> None:
        self.player_list = [
            Player('Captain Ahmed'), Player('The Golden God'), Player('Cheen')
        ]

        for player in self.player_list:
            loader = DataLoader(player.player_name)
            stats = loader.get_cleaned_matches()
            player.process_stats(stats)

        self.awards = WeezAwards(self.player_list)

    def test_award_attributes(self) -> None:
        """
        Process the Awards and check that the attributes created are correct.
        :return: None.
        """
        self.awards.process_player_stats()
        assert self.awards.bullet_bitch == 'The Golden God'
        assert self.awards.medic is None
        assert self.awards.head_master == 'The Golden God'
        assert self.awards.top_assister == 'The Golden God'
        assert self.awards.team_lover == 'The Golden God'
        assert self.awards.team_hater == 'Cheen'
        assert self.awards.lethal_killer == 'Captain Ahmed'
        assert self.awards.least_lethal_killer == 'Cheen'
        assert self.awards.tank == 'Cheen'
        assert self.awards.team_demolisher is None
        assert self.awards.big_spender is None
        assert self.awards.hungry_bitch is None
        assert self.awards.pussio == 'Cheen'

    def test_player_results(self) -> None:
        """
        Process the awards message and check that it is equal to the expected
        message.
        :return: None.
        """
        with open('Data/expected_awards.txt') as expected_file:
            expected = expected_file.read()

        self.awards.process_player_stats()
        actual = self.awards.show_player_results()
        assert actual == expected
        print(actual)
