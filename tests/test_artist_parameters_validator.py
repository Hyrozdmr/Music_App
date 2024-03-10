import pytest
from lib.artist_parameters_validator import ArtistParametersValidator


"""
With A valid name and year
It is valid
"""
def test_is_valid():
    validator = ArtistParametersValidator("My Name", "Genre")
    assert validator.is_valid() == True


"""
With A blank or None name
It is not valid
"""
def test_is_not_valid_with_bad_name():
    validator_1 = ArtistParametersValidator("", "Genre")
    assert validator_1.is_valid() == False
    validator_2 = ArtistParametersValidator(None, "Genre")
    assert validator_2.is_valid() == False

"""
With A blank or None genre
It is not valid
"""
def test_is_not_valid_with_bad_genre():
    validator_1 = ArtistParametersValidator("My Name", "")
    assert validator_1.is_valid() == False
    validator_2 = ArtistParametersValidator("My Name", None)
    assert validator_2.is_valid() == False


"""
With invalid parameters
Produces errors
"""
def test_generate_errors():
    validator_1 = ArtistParametersValidator("", "")
    assert validator_1.generate_errors() == [
        "Name must not be blank",
        "Genre must not be blank"
    ]

    validator_2 = ArtistParametersValidator("", "Genre")
    assert validator_2.generate_errors() == [
        "Name must not be blank"
    ]
    
    validator_3 = ArtistParametersValidator("Name", "")
    assert validator_3.generate_errors() == [
        "Genre must not be blank"
    ]


def test_get_valid_name_if_name_valid():
    validator_1 = ArtistParametersValidator("Name", "Genre")
    assert validator_1.get_valid_name() == "Name"

def test_get_valid_name_refuses_if_invalid():
    validator_1 = ArtistParametersValidator("", "Name")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_name()
    assert str(err.value) == "Cannot get valid name"


def test_get_valid_genre_if_genre_valid():
    validator_1 = ArtistParametersValidator("Name", "Genre")
    assert validator_1.get_valid_genre() == "Genre"

def test_get_valid_genre_refuses_if_invalid():
    validator_1 = ArtistParametersValidator("Name", "")
    with pytest.raises(ValueError) as err:
        validator_1.get_valid_genre()
    assert str(err.value) == "Cannot get valid genre"
