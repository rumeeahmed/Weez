import json


class DataLoader:
    """
    Object that handles the loading of data for tests.
    """

    def __init__(self, player_name: str):
        """

        :param player_name: a string object that represents the player's dataset
        """
        self.player_name = player_name.lower().replace(' ', '_')
        with open(f'Data/{self.player_name}_test_data.json') as test_file:
            self.data = json.load(test_file)

    def get_matches(self) -> dict:
        """
        Get all the matches for the current player.
        :return: a dictionary object containing all the matches for the current
        player.
        """
        return self.data['data']['matches']

    def get_current_matches(self) -> list:
        """
        Get all the current matches for the current player.
        :return: a list of matches played on the last date for the current
        player.
        """
        matches = self.get_matches()
        latest_timestamp = matches[0]['metadata']['timestamp'].split('T')[0]
        current_matches = []
        for match in matches:
            match_timestamp = match['metadata']['timestamp'].split('T')[0]
            if match_timestamp == latest_timestamp:
                current_matches.append(match)
        return current_matches

    def get_cleaned_matches(self) -> list:
        """
        Get only the stats for the last set of matches for the current player.
        :return: a list object containing only the stats for the current
        matches.
        """
        data = []
        matches = self.get_current_matches()
        for match in matches:
            cleaned_stat = {}
            stats = match['segments'][0]['stats']

            for key, value in stats.items():
                cleaned_stat[key] = value['value']
            data.append(cleaned_stat)
        return data
