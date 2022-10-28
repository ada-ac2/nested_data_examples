'''
Now that we know what the pokedex data looks like, let's write a function
that uses it. 

How could we get a list of all the unique pokemon types in pokedex?
Let's write the function `get_all_pokemon_types` together. It should
return a data structure that contains every pokemon type in pokedex
without holding any duplicate values.

As we write `get_all_pokemon_types`, keep an eye out for tasks we 
could move to a helper function.
'''

def get_all_pokemon_types(pokedex):
    all_types = set()

    for key in pokedex:
        types = get_types_by_id(pokedex, key)
        all_types.update(types)

    return all_types

def get_types_by_id(pokedex, id):
    return pokedex[id]["types"]


test_tuple = (1, 2)
new_tuple = test_tuple * 3
print(new_tuple)

'''
The import line needs to be commented out for the tests to run
without encountering an import error. This has to do with how pytest 
searches paths for resources. If you want to know more about what's 
happening, I recommend searching for how python and pytest resolves imports.
'''
# from pokedex_nested_data import pokedex
# print(get_all_pokemon_types(pokedex))