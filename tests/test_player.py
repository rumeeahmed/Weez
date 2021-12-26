from AnalysisTools.weez_reader import Player
from unittest import TestCase
import json


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
        with open("test_data.json", "r") as content:
            self.data = json.load(content)

    def test_unit(self) -> None:
        """
        Test the properties of the scraper object.
        :return: None.
        """
        assert self.player.player_name == 'The Golden God'
        assert self.player.judge is False
        assert self.player.gn is None
