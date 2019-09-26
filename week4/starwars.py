#StarWars simple demo

import requests
import json

base_people_url = 'https://swapi.co/api/people'
species_types = {'https://swapi.co/api/species/1/': 'Human',
                 'https://swapi.co/api/species/2/': 'Droid',
                 'https://swapi.co/api/species/3/': 'Wookiee'}

def get_species_name(key_url):
    return species_types[key_url]

class Character:

    def __init__(self, name="Luke Skywalker",
                 species="Human",
                 json_dict=None ):

        if json_dict is None:
            # we are hand-constructed
            self.name = name
            self.species = species
        else:
            self.process_json_dict(json_dict)

    def process_json_dict(self, json_dict):
        self.name = json_dict['name']
        species_url = json_dict['species'][0]
        if species_url in species_types:
            # print(species_url)
            self.species = get_species_name(species_url)
        else:
            self.species = 'Other'

    def __str__(self):
        return self.name + ' (' + self.species + ')'

    def __repr__(self):
        return self.name + ' (' + self.species + ')'

class Human(Character):
 
    def __init__(self, name='Luke Skywalker',
                 species='Human', eye_color='Brown',
                 json_dict=None):
        super().__init__(name, species, json_dict)
        if json_dict is not None:
            self.eye_color = json_dict['eye_color']
        else:
            self.eye_color = eye_color
 
    def __str__(self):
        return super().__str__() + ', eye color: ' + self.eye_color

# class Jedi(Human)
'''
If you see a character whose name starts with Luke or
  Obi-wan, make them into a Jedi
The Jedi constructor should delegate to the super( )
  constructor (Human), but add one instance variable:
  has_light_saber = True
Override __str__( ) so that something additional
  prints out for Jedis that lets us know they are
  Jedis (but all the old stuff should print out. And
  remember to stay DRY!
'''

dummy_char = Character('Jabba', 'Hutt')
print(dummy_char)

json_string = requests.get(base_people_url).text
results_list = json.loads(json_string)['results']

characters = []
for r in results_list:
    # print(r)
    if get_species_name(r['species'][0]) == "Human":
        c = Human(json_dict=r)
    else:
        c = Character(json_dict=r)
    characters.append(c)

for c in characters:
    print(c)