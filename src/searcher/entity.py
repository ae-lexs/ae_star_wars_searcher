import json
from http import HTTPStatus

from dataclasses import dataclass


@dataclass
class Character(object):
    birth_year: str
    homeworld: str
    name: str
    species: str
    url: str

    def to_dict(self):
        return {
            'birth_year': self.birth_year,
            'homeworld': self.homeworld,
            'name': self.name,
            'species': self.species,
            'url': self.url,
        }


@dataclass
class Response(object):
    statusCode: HTTPStatus
    data: list

    def to_json(self):
        return json.dumps({
            'statusCode': self.statusCode,
            'data': self.data,
        })
