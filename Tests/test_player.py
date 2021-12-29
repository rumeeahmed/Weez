from AnalysisTools.weez_reader import Player
from Tests.data_loader import DataLoader
from unittest import TestCase


class TestReader(TestCase):
    """
    Object that tests the `Player` object.
    """

    def setUp(self) -> None:
        """
        Set up a test scraper object for every test.
        :return: None.
        """
        self.player = Player('The Golden God')
        self.loader = DataLoader('Captain Ahmed')
        self.data = self.loader.get_cleaned_matches()

    def test_unit(self) -> None:
        """
        Test the properties of the player object.
        :return: None.
        """
        assert self.player.player_name == 'The Golden God'
        assert self.player.judge is False
        assert self.player.gn is None

    def test_process_stats(self) -> None:
        """
        Process the Players stats and check that the processed attributes are
        correct.
        :return: None
        """

        self.player.process_stats(self.data)

        assert self.player.player_name == 'The Golden God'
        assert self.player.kills == 4
        assert self.player.assists == 2
        assert self.player.deaths == 12
        assert self.player.games_played == 6
        assert self.player.damage == 1580
        assert self.player.damage_taken == 2133
        assert self.player.headshots == 0
        assert self.player.kd == 0.33
        assert self.player.distance_travelled == 2403748
        assert self.player.score == 11525
        assert self.player.revives == 0
        assert self.player.crates_opened == 0
        assert self.player.shop_buys == 0
        assert self.player.time_moving == 70
        assert self.player.date is None

    def test_get_stats(self) -> None:
        """
        Check that the return value of the `get_stats` method is equal to the
        expected value.
        :return: None.
        """
        with open('Data/expected_player_stats.txt') as expected_file:
            expected = expected_file.read()
        self.player.process_stats(self.data)
        actual = self.player.get_stats()
        assert actual == expected
