from AnalysisTools.weez_reader import Team
from unittest import TestCase
import json


class TestTeam(TestCase):
    """
    Object that tests the Team object.
    """

    def setUp(self) -> None:
        player_list = []
