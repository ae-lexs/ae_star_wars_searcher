import json

from src.searcher.handler import Searcher

class TestSearcher(object):
    def test_search(self):
        expected_response = json.dumps({
            'statusCode': 200,
            'data': [
                {
                    'birth_year': 'R2-D2',
                    'homeworld': 'Naboo',
                    'name': 'R2-D2',
                    'species': 'Droid',
                    'url': 'https://swapi.dev/api/people/3/',
                },
            ],
        })

        actual_response = Searcher.search(
            keyword='r2',
        )

        assert actual_response == expected_response
