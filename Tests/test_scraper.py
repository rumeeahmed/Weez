from Scraper.weez_scraper import WeezScraper
from Tests.data_loader import DataLoader
from unittest.mock import patch
from datetime import datetime
from unittest import TestCase


class TestScraper(TestCase):
    """
    Object that tests the `WeezScraper` object.
    """

    def setUp(self) -> None:
        """
        Set up a test scraper object for every test.
        :return: None
        """
        self.scraper = WeezScraper('Buttpunch69#5164309', 'atvi')
        self.loader = DataLoader('Captain Ahmed')

    def test_unit(self) -> None:
        """
        Test the properties of the scraper object.
        :return: None
        """
        assert self.scraper.username == 'Buttpunch69#5164309'
        assert self.scraper.platform == 'atvi'

    def test_construct_timestamp(self) -> None:
        """
        Test that the scraper objects timestamp is equal to the current
        timestamp.
        :return: None.
        """
        self.scraper._construct_timestamp()
        now = datetime.now().timestamp()
        timestamp = round(now) * 1000
        assert self.scraper._timestamp == timestamp

    def test_build_url(self) -> None:
        """
        Test that the url that is created and then called is equal to the
        expected url.
        :return: None.
        """
        self.scraper._build_url()
        expected = 'https://api.tracker.gg/api/v2/warzone/standard/matches/' \
                   'atvi/Buttpunch69%235164309'
        assert self.scraper._url == expected

    def test_get_matches(self) -> None:
        """
        Test the functionality of the `_get_matches` method in the Scraper
        object. First, check that the `_build_url`, `_construct_timestamp` and
        `_get_matches` methods are called. Then check that the returned data is
        a list with 20 items.
        :return: None.
        """

        data = self.loader.get_matches()

        with patch(
            'Scraper.weez_scraper.WeezScraper._build_url'
        ) as mocked_url, patch(
            'Scraper.weez_scraper.WeezScraper._construct_timestamp'
        ) as mocked_timestamp, patch(
            'Scraper.weez_scraper.WeezScraper._get_matches', return_value=data,
            side_effects=[
                self.scraper._build_url(), self.scraper._construct_timestamp(),
            ]
        ) as mocked_matches:

            actual = self.scraper._get_matches()
            mocked_matches.assert_called_once()
            mocked_url.assert_called_once()
            mocked_timestamp.assert_called_once()
            assert type(actual) == list
            assert len(actual) == 20

    def test_get_current_matches(self) -> None:
        """
        Test the functionality of the `_get_current_matches` method in the
        Scraper object. First, check that the `_get_current_matches`,
        `_get_matches`, `_construct_timestamp` and `_build_url` methods are
        called. Then check that the returned data is a list with 6 items.
        :return: None.
        """
        matches = self.loader.get_current_matches()

        with patch(
            'Scraper.weez_scraper.WeezScraper._build_url'
        ) as mocked_url, patch(
            'Scraper.weez_scraper.WeezScraper._construct_timestamp'
        ) as mocked_timestamp, patch(
            'Scraper.weez_scraper.WeezScraper._get_matches',
            side_effects=[
                self.scraper._build_url(), self.scraper._construct_timestamp(),
            ]
        ) as mocked_matches, patch(
            'Scraper.weez_scraper.WeezScraper._get_current_matches',
            return_value=matches, side_effects=self.scraper._get_matches()
        ) as mocked_current_matches:

            actual = self.scraper._get_current_matches()
            mocked_current_matches.assert_called_once()
            mocked_matches.assert_called_once()
            mocked_timestamp.assert_called_once()
            mocked_url.assert_called_once()
            assert type(actual) == list
            assert len(actual) == 6

    def test_extract_match_stats(self) -> None:
        """
        Test the functionality of the `_test_extract_match_stats` method in the
        Scraper object. First, check that the `_extract_match_stats`,
        `_get_current_matches`, `_get_matches`, `_construct_timestamp` and
        `_build_url` methods are called. Then check that the returned data is a
        list with 6 items. Each one of these items should be a dict and must
        contain the specified keys.
        :return: None.
        """
        matches = self.loader.get_current_matches()
        data = []
        for match in matches:
            stats = match['segments'][0]['stats']
            data.append(stats)

        with patch(
            'Scraper.weez_scraper.WeezScraper._build_url'
        ) as mocked_url, patch(
            'Scraper.weez_scraper.WeezScraper._construct_timestamp'
        ) as mocked_timestamp, patch(
            'Scraper.weez_scraper.WeezScraper._get_matches',
            side_effects=[
                self.scraper._build_url(), self.scraper._construct_timestamp(),
            ]
        ) as mocked_matches, patch(
            'Scraper.weez_scraper.WeezScraper._get_current_matches',
            side_effects=self.scraper._get_matches()
        ) as mocked_current_matches, patch(
            'Scraper.weez_scraper.WeezScraper._extract_match_stats',
            return_value=data, side_effects=self.scraper._get_current_matches()
        ) as mocked_extract:

            actual = self.scraper._extract_match_stats()
            match = actual[0]

            mocked_current_matches.assert_called_once()
            mocked_matches.assert_called_once()
            mocked_timestamp.assert_called_once()
            mocked_url.assert_called_once()
            mocked_extract.assert_called_once()

            assert type(actual) == list
            assert len(actual) == 6
            assert type(match) == dict
            assert 'kills' in match
            assert 'score' in match
            assert 'headshots' in match
            assert 'assists' in match
            assert 'distanceTraveled' in match
            assert 'deaths' in match
            assert 'kdRatio' in match
            assert 'percentTimeMoving' in match
            assert 'damageDone' in match
            assert 'damageTaken' in match

    def test_scrape(self) -> None:
        """
        Test the functionality of the `scrape` method in the Scraper object.
        First, check that the `scrape`, `_extract_match_stats`,
        `_get_current_matches`, `_get_matches`, `_construct_timestamp` and
        `_build_url` methods are called. Then check that the returned data is a
        list with 6 items. Each one of these items should be a dict and must
        contain the specified keys.
        :return: None.
        """
        matches = self.loader.get_current_matches()
        data = []

        for match in matches:
            cleaned_stat = {}
            stats = match['segments'][0]['stats']

            for key, value in stats.items():
                cleaned_stat[key] = value['value']
            data.append(cleaned_stat)

        with patch(
            'Scraper.weez_scraper.WeezScraper._build_url'
        ) as mocked_url, patch(
            'Scraper.weez_scraper.WeezScraper._construct_timestamp'
        ) as mocked_timestamp, patch(
            'Scraper.weez_scraper.WeezScraper._get_matches',
            side_effects=[
                self.scraper._build_url(), self.scraper._construct_timestamp(),
            ]
        ) as mocked_matches, patch(
            'Scraper.weez_scraper.WeezScraper._get_current_matches',
            side_effects=self.scraper._get_matches()
        ) as mocked_current_matches, patch(
            'Scraper.weez_scraper.WeezScraper._extract_match_stats',
            side_effects=self.scraper._get_current_matches()
        ) as mocked_extract, patch(
            'Scraper.weez_scraper.WeezScraper.scrape',
            side_effets=self.scraper._extract_match_stats()
        ) as mocked_scrape:

            self.scraper.scrape()
            self.scraper.stats = data
            match = self.scraper.stats[0]

            mocked_current_matches.assert_called_once()
            mocked_matches.assert_called_once()
            mocked_timestamp.assert_called_once()
            mocked_url.assert_called_once()
            mocked_extract.assert_called_once()
            mocked_scrape.assert_called_once()

            assert type(self.scraper.stats) == list
            assert len(self.scraper.stats) == 6
            assert 'kills' in match
            assert 'score' in match
            assert 'headshots' in match
            assert 'assists' in match
            assert 'distanceTraveled' in match
            assert 'deaths' in match
            assert 'kdRatio' in match
            assert 'percentTimeMoving' in match
            assert 'damageDone' in match
            assert 'damageTaken' in match
            