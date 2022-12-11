'''
{
    "characters": [
        "https://swapi.dev/api/people/1/",
        ...
    ],
    "created": "2014-12-10T14:23:31.880000Z",
    "director": "George Lucas",
    "edited": "2014-12-12T11:24:39.858000Z",
    "episode_id": 4,
    "opening_crawl": "It is a period of civil war.\n\nRebel spaceships, striking\n\nfrom a hidden base, have won\n\ntheir first victory against\n\nthe evil Galactic Empire.\n\n\n\nDuring the battle, Rebel\n\nspies managed to steal secret\r\nplans to the Empire's\n\nultimate weapon, the DEATH\n\nSTAR, an armored space\n\nstation with enough power\n\nto destroy an entire planet.\n\n\n\nPursued by the Empire's\n\nsinister agents, Princess\n\nLeia races home aboard her\n\nstarship, custodian of the\n\nstolen plans that can save her\n\npeople and restore\n\nfreedom to the galaxy....",
    "planets": [
        "https://swapi.dev/api/planets/1/",
        ...
    ],
    "producer": "Gary Kurtz, Rick McCallum",
    "release_date": "1977-05-25",
    "species": [
        "https://swapi.dev/api/species/1/",
        ...
    ],
    "starships": [
        "https://swapi.dev/api/starships/2/",
        ...
    ],
    "title": "A New Hope",
    "url": "https://swapi.dev/api/films/1/",
    "vehicles": [
        "https://swapi.dev/api/vehicles/4/",
        ...
    ]
}
'''


from models.basemodels import Base
from typing import Optional, List

class Films(Base):
    characters: Optional[list[str]]
    director: str
    episode_id: int
    opening_crawl: str
    planets: Optional[List[str]]
    producer: str
    release_date: str
    species: Optional[List[str]]
    starships: Optional[List[str]]
    title: str
    vehicles: Optional[List[str]]
a={
	"title": "A New Hope",
	"episode_id": 4,
	"opening_crawl": "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\ntheir first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\nspies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\nSTAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\nPursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\nstarship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\nfreedom to the galaxy....",
	"director": "George Lucas",
	"producer": "Gary Kurtz, Rick McCallum",
	"release_date": "1977-05-25",
	"characters": [
		"https://swapi.dev/api/people/1/",
		"https://swapi.dev/api/people/2/",
		"https://swapi.dev/api/people/3/",
		"https://swapi.dev/api/people/4/",
		"https://swapi.dev/api/people/5/",
		"https://swapi.dev/api/people/6/",
		"https://swapi.dev/api/people/7/",
		"https://swapi.dev/api/people/8/",
		"https://swapi.dev/api/people/9/",
		"https://swapi.dev/api/people/10/",
		"https://swapi.dev/api/people/12/",
		"https://swapi.dev/api/people/13/",
		"https://swapi.dev/api/people/14/",
		"https://swapi.dev/api/people/15/",
		"https://swapi.dev/api/people/16/",
		"https://swapi.dev/api/people/18/",
		"https://swapi.dev/api/people/19/",
		"https://swapi.dev/api/people/81/"
	],
	"planets": [
		"https://swapi.dev/api/planets/1/",
		"https://swapi.dev/api/planets/2/",
		"https://swapi.dev/api/planets/3/"
	],
	"starships": [
		"https://swapi.dev/api/starships/2/",
		"https://swapi.dev/api/starships/3/",
		"https://swapi.dev/api/starships/5/",
		"https://swapi.dev/api/starships/9/",
		"https://swapi.dev/api/starships/10/",
		"https://swapi.dev/api/starships/11/",
		"https://swapi.dev/api/starships/12/",
		"https://swapi.dev/api/starships/13/"
	],
	"vehicles": [
		"https://swapi.dev/api/vehicles/4/",
		"https://swapi.dev/api/vehicles/6/",
		"https://swapi.dev/api/vehicles/7/",
		"https://swapi.dev/api/vehicles/8/"
	],
	"species": [
		"https://swapi.dev/api/species/1/",
		"https://swapi.dev/api/species/2/",
		"https://swapi.dev/api/species/3/",
		"https://swapi.dev/api/species/4/",
		"https://swapi.dev/api/species/5/"
	],
	"created": "2014-12-10T14:23:31.880000Z",
	"edited": "2014-12-20T19:49:45.256000Z",
	"url": "https://swapi.dev/api/films/1/"
}

b=Films(**a)
print(b)









