from AnalysisTools.weez_analysis import GNCalculator
from AnalysisTools.weez_reader import Player
from Tests.data_loader import DataLoader
from unittest.mock import patch
from unittest import TestCase


class TestGNCalculator(TestCase):
    """
    Object that tests the GNCalculator object.
    """

    def setUp(self) -> None:
        """
        Set up a test GNCalculator object for every test.
        :return: None.
        """

        self.player = Player('Captain Ahmed')
        self.loader = DataLoader(self.player.player_name)
        self.data = self.loader.get_cleaned_matches()
        self.player.process_stats(self.data)
        self.gn_calculator = GNCalculator(self.player)

    def test_get_damage_gn(self) -> None:
        """
        Test the `get_damage_gn` method in the GNCaluclator object.
        :return: None.
        """
        games_played = self.player.games_played
        if self.player.player_name == 'The Golden God':
            damage_gn = games_played * 900
        else:
            damage_gn = games_played * 750

        with patch(
            'AnalysisTools.weez_analysis.GNCalculator.get_damage_gn',
            return_value=damage_gn
        ):
            actual_damage_gn = self.gn_calculator.get_damage_gn()
            assert actual_damage_gn == 5400

    def test_gn_judgement_true(self) -> None:
        """
        Test the `gn_judgement`, the value returned should be true as the
        Players gn is lower than their damage.
        :return: None.
        """
        self.player.gn = 1000
        actual = self.gn_calculator.gn_judgement()
        assert actual is True

    def test_gn_judgement_false(self) -> None:
        """
        Test the `gn_judgement`, the value returned should be false as the
        Players gn is higher than their damage.
        :return: None.
        """
        self.player.gn = 2000
        actual = self.gn_calculator.gn_judgement()
        assert actual is False
