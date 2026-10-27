import random
from time import sleep
import requests
from os import path
from bs4 import BeautifulSoup
from PIL import Image
from _config import getPath

# read cached website
site = open(getPath("pokemon.html"), encoding="utf-8").read()
soup = BeautifulSoup(site, "html.parser")

# get all pokemon (each list is a different gen)
lists = soup.find_all(name="div", class_="infocard-list")
gen1 = lists[0].find_all(name="div")

def get_pokemon(elem):
    # get name
    name = elem.find(class_="ent-name").text

    # try using cache...
    pathToImage = getPath(name + ".jfif")

    # but if it doesn't exist download it
    if not path.exists(pathToImage):
        print("Fetching image...")
        image = elem.find(class_="img-fixed img-sprite")
        src = image["src"]
        # download image
        with open(pathToImage, "wb") as file:
            req = requests.get(src)
            file.write(req.content)

            # we want to avoid stressing the server, so we wait before sending
            # another request
            sleep(1)

    return { "name": name, "pathToImage": pathToImage }

def get_rdm_pokemon_list(amt):
    pokemon_list = []
    chosen = set()
    while amt > 0 and len(gen1) != len(pokemon_list):
        elem = random.choice(gen1)
        pokemon = get_pokemon(elem)
        # skip if this one's already in the list
        if pokemon["name"] in chosen:
            continue
        chosen.add(pokemon["name"])
        pokemon_list.append(pokemon)
        amt -= 1

    return pokemon_list

# generate random pokemon
options = get_rdm_pokemon_list(4)
correctPokemon = options[0]
img = Image.open(correctPokemon["pathToImage"])

# shuffle and display
random.shuffle(options)
print("Who's that Pokémon?")
code: str = 'A'
for pokemon in options:
    print(f"{code} - {pokemon["name"]}")
    code = chr(ord(code) + 1)
img.show()

# get user's answer
answer = input().strip().upper()
chosen = options[ord(answer) - ord('A')]
print(f"You chose {chosen["name"]}...")
if chosen == correctPokemon:
    print("That's correct!")
else:
    print(f"But it was {correctPokemon["name"]}!")
