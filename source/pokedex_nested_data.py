'''
If we've created a data structure, we can take a look
at the construction and map it out on paper if that helps
our understanding.

Take a look at the variables set up below, then try to map
out the structure of the data that `pokedex` points to.
'''

bulbasaur_entry = {
    "name": "Bulbasaur",
    "description": "Seed Pokemon"
}
bulbasaur_entry["types"] = ["Grass", "Poison"]

charmander_entry = {
    "types": ["Fire"],
    "description": "Fire Pokemon"
}
charmander_entry["name"] = "Charmander"

squirtle_entry = {
    "name": "Squirtle",
    "types": ["Water"]
}
squirtle_entry["description"] = "Tiny Turtle Pokemon"

gastly_entry = {
    "name": "Gastly",
    "description": "Gas Pokemon"
}
gastly_entry["types"] = ["Ghost", "Poison"]

pokedex = {
    1: bulbasaur_entry,
    4: charmander_entry,
    7: squirtle_entry,
    91: gastly_entry
}


'''
What is the final structure of the `pokedex`? Let's map it out!

pokedex = {
    1: {
        "name": "Bulbasaur"
        "description": "Seed Pokemon"
        "type": ["Grass", "Poison"]
    }
    4: {
        "name": "Charmander"
        "description": "Fire Pokemon"
        "type": ["Fire"]
    }
    7: {
        "name": "Squirtle",
        "types": ["Water"],
        "description": "Tiny Turtle Pokemon"
    }
    91: {
        "name": "Gastly"
        "description": "Gas Pokemon"
        "type": ["Ghost", "Poison"]
    }
}
'''