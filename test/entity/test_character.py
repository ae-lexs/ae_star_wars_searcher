from src.searcher.entity import Character


class TestCharacter(object):
    def test_to_dict(self):
        expected_character = {
            'birth_year': 'R2-D2',
            'homeworld': 'Naboo',
            'name': 'R2-D2',
            'species': 'Droid',
            'url': 'https://swapi.dev/api/people/3/',
        }

        actual_character = Character(
            birth_year='R2-D2',
            homeworld='Naboo',
            name='R2-D2',
            species='Droid',
            url='https://swapi.dev/api/people/3/',
        ).to_dict()

        assert actual_character == expected_character
