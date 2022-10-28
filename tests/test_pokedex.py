import pytest

from source.pokedex_nested_data import bulbasaur_entry, charmander_entry, pokedex
from source.pokedex_tools import get_all_pokemon_types, get_types_by_id


def test_get_all_pokemon_types_empty_pokedex():
    # Arrange data
    test_pokedex = {}

    # Act
    result = get_all_pokemon_types(test_pokedex)

    # Assert
    assert len(result) == 0

def test_get_all_pokemon_types_one_pokemon_in_pokedex():
    # Arrange data
    test_pokedex = { 4: charmander_entry }

    # Act
    result = get_all_pokemon_types(test_pokedex)

    # Assert
    assert len(result) == 1
    assert "Fire" in result

def test_get_all_pokemon_types_many_pokemon_in_pokedex():
    # Act
    result = get_all_pokemon_types(pokedex)

    # Assert
    assert len(result) == 5
    assert "Fire" in result
    assert "Poison" in result
    assert "Ghost" in result
    assert "Grass" in result
    assert "Water" in result

@pytest.mark.skip
def test_get_types_by_id_one_pokemon_in_pokedex():
    # Arrange data
    test_pokedex = { 1: bulbasaur_entry }

    # Act
    result = get_types_by_id(test_pokedex, 1)

    # Assert
    assert len(result) == 2
    assert "Grass" in result
    assert "Poison" in result

@pytest.mark.skip
def test_get_types_by_id_many_pokemon_in_pokedex():
    # Act
    result = get_types_by_id(pokedex, 91)

    # Assert
    assert len(result) == 2
    assert "Poison" in result
    assert "Ghost" in result

@pytest.mark.skip
def test_get_types_by_id_pokemon_missing_from_pokedex():
    # Arrange data
    test_pokedex = { 1: bulbasaur_entry }
    
    # Act
    with pytest.raises(KeyError):
        result = get_types_by_id(test_pokedex, 4)
