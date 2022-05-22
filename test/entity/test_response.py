import json
from http import HTTPStatus

from src.searcher.entity import Character, Response


def test_to_json():
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

    actual_response = Response(
        statusCode=HTTPStatus.OK,
        data=[
            Character(
                birth_year='R2-D2',
                homeworld='Naboo',
                name='R2-D2',
                species='Droid',
                url='https://swapi.dev/api/people/3/',
            ).to_dict(),
        ],
    ).to_json()

    assert actual_response == expected_response

