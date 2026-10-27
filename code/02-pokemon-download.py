import requests
from _config import getPath

# download pokemon website
url = "https://pokemondb.net/pokedex/national"

with open(getPath("pokemon.html"), 'w') as p:
    p.write(requests.get(url).text)
