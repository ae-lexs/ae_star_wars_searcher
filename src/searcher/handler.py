from http import HTTPStatus

from src.searcher.entity import Character, Response


class Searcher(object):
    def search(keyword: str) -> Response:
        return Response(
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
